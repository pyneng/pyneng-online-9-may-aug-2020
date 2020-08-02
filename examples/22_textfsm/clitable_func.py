# или import clitable, если версия textfsm == 0.4
from textfsm import clitable


def parse_output(command, output, vendor=None):
    cli = clitable.CliTable("index", "templates")
    attributes = {"Command": command}
    if vendor:
        attributes = {"Command": command, "Vendor": vendor}

    cli.ParseCmd(output, attributes)

    data_rows = [list(row) for row in cli]
    return data_rows
