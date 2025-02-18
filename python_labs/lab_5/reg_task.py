import json
import re

file_path = "row.txt"
# Read the entire file as a single string
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

receipt_data = {
    "Филиал" : None,
    "БИН" : None,
    "Кассир" : None,
    "Смена" : None,
    "Порядковый номер чека" : None,
    "Чек" : None,
    "Продукты" : [],
    "Итого" : None,
    "Бансковская карта" : None,
    "Время" : None,
    "НДС Серия" : None,
    "№" : None,
    "ИНК ОФД" : None,
    "Код ККМ КГД (РНМ)" : None,
    "ЗНМ" : None,
    "Фискальный признак" : None,
    "Касса" : None
}

# 1. Parse single-line fields
#
# Each regex below looks for a line that starts with a specific label and captures the rest of that line.
# For example, '^Филиал\s+(.*)$' means:
#  - ^       Start of line
#  - Филиал  The word "Филиал"
#  - \s+     One or more spaces
#  - (.*)    Capture all remaining characters in that line
#  - $       End of line
# The re.MULTILINE flag makes ^/$ match the start/end of each line rather than the entire string.

match = re.search(r'^Филиал\s+(.*)$', text, re.MULTILINE)
if match:
    receipt_data["Филиал"] = match.group(1).strip()

match = re.search(r'^БИН\s+(\d+)$', text, re.MULTILINE)
if match:
    receipt_data["БИН"] = match.group(1)

match = re.search(r'^Кассир\s+(.*)$', text, re.MULTILINE)
if match:
    receipt_data["Кассир"] = match.group(1).strip()

match = re.search(r'^Смена\s+(\d+)$', text, re.MULTILINE)
if match:
    receipt_data["Смена"] = match.group(1)

match = re.search(r'^Порядковый номер чека\s+№(\d+)$', text, re.MULTILINE)
if match:
    receipt_data["Порядковый номер чека"] = match.group(1)

match = re.search(r'^Чек\s+№(\d+)$', text, re.MULTILINE)
if match:
    receipt_data["Чек"] = match.group(1)

match = re.search(r'^НДС Серия\s+(\d+)$', text, re.MULTILINE)
if match:
    receipt_data["НДС Серия"] = match.group(1)

match = re.search(r'^\s*№\s+(\d+)$', text, re.MULTILINE)
if match:
    receipt_data["№"] = match.group(1)

match = re.search(r'^Касса\s+([\d-]+)$', text, re.MULTILINE)
if match:
    receipt_data["Касса"] = match.group(1)

match = re.search(r'^Банковская карта:\s+([\d,\.]+)$', text, re.MULTILINE)
if match:
    receipt_data["Бансковская карта"] = match.group(1)

match = re.search(r'^ИТОГО:\s+([\d,\.]+)$', text, re.MULTILINE)
if match:
    receipt_data["Итого"] = match.group(1)

# Look for a line like 'Время: 18.04.2019 11:13:58'
match = re.search(r'^Время:\s+(.*)$', text, re.MULTILINE)
if match:
    receipt_data["Время"] = match.group(1).strip()

match = re.search(r'^Фискальный признак:\s*(\d+)$', text, re.MULTILINE)
if match:
    receipt_data["Фискальный признак"] = match.group(1)

match = re.search(r'^ИНК ОФД:\s*(\d+)$', text, re.MULTILINE)
if match:
    receipt_data["ИНК ОФД"] = match.group(1)

match = re.search(r'^Код ККМ КГД \(РНМ\):\s*(\d+)$', text, re.MULTILINE)
if match:
    receipt_data["Код ККМ КГД (РНМ)"] = match.group(1)

match = re.search(r'^ЗНМ:\s*(\S+)$', text, re.MULTILINE)
if match:
    receipt_data["ЗНМ"] = match.group(1)

# 2. Parse Products
#
# The products appear after the line "ПРОДАЖА" and follow a pattern like:
#   1.
#   Натрия хлорид 0,9%, 200 мл, фл
#   2,000 x 154,00
#   308,00
#   Стоимость
#   308,00
#   ...
#
# One approach is to use a block-based regex that:
# - Finds lines with a number and a period (like "1.")
# - Captures the product name (possibly spanning lines)
# - Captures quantity/unit price
# - Captures the subtotal(s)
#
# In practice, you may have to tweak this pattern if your text differs.
#
# We will do this by capturing "item blocks": from lines like "\d+\." up to
# the next "\d+\." or the end of the "ПРОДАЖА" section.

# First, let's isolate the text that starts from "ПРОДАЖА" up to some marker (e.g., "Банковская карта:" or "ИТОГО:"), 
# so we only parse product lines in that region.

# We can do a lazy approach: find everything from "ПРОДАЖА" up to "Банковская карта:" or "ИТОГО:"
sales_section_match = re.search(r'ПРОДАЖА\s*(.*?)\s*(?=Банковская карта:|ИТОГО:|$)', text, re.DOTALL)
if sales_section_match:
    sales_section = sales_section_match.group(1)
else:
    sales_section = ""

# Now parse item blocks within the sales section.
# A straightforward pattern might be:
#    (?P<number>^\d+\.)   # e.g. '1.'
#    (.*?)                # The lines up until the next item number or end
# We'll use a "split" approach or a "finditer" approach.

item_pattern = re.compile(
    r'(?P<number>^\d+\.)\s*(?P<content>.*?)(?=^\d+\.|$)',
    re.MULTILINE | re.DOTALL
)

items = item_pattern.finditer(sales_section)

product_list = []
for item in items:
    item_number = item.group('number').strip()
    content = item.group('content').strip()

    # Example: inside "content", you might see:
    #   Натрия хлорид 0,9%, 200 мл, фл
    #   2,000 x 154,00
    #   308,00
    #   Стоимость
    #   308,00
    #
    # Let's capture lines more explicitly:

    # Extract the first line as product name
    # Then look for quantity & unit price in "2,000 x 154,00"
    # Then look for the next line as "308,00"
    lines = content.splitlines()
    # Be careful with indexes in case data is missing or lines vary in count
    product_name = lines[0].strip() if len(lines) > 0 else ""
    
    # Regex for "2,000 x 154,00"
    # We'll default to quantity=None, unit_price=None if we don't find them
    quantity, unit_price = None, None
    match_qp = re.search(r'([\d,]+)\s*x\s*([\d,]+)', content)
    if match_qp:
        quantity = match_qp.group(1)
        unit_price = match_qp.group(2)
    
    # Look for a subtotal line, e.g. "308,00"
    # We'll assume the first line that looks like a price with comma is the subtotal
    subtotal_pattern = re.compile(r'(\d{1,3}(?:\.\d{3}|\,\d+)+)')
    subtotal_match = subtotal_pattern.search(content)
    subtotal = subtotal_match.group(1) if subtotal_match else None

    product_list.append({
        "Номер": item_number.replace('.', ''),
        "Наименование": product_name,
        "Количество": quantity,
        "Цена за единицу": unit_price,
        "Сумма": subtotal
    })

receipt_data["Продукты"] = product_list

# 3. Print or Save to JSON
print(json.dumps(receipt_data, ensure_ascii=False, indent=4))


print("Don't forget changes!")
print("Today was difficult day")