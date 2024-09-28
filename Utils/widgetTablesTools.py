def get_selected_row_data(tableWidget):
    selected_rows = tableWidget.selectionModel().selectedRows()  # Get selected rows
    selected_data = []

    for row_index in selected_rows:
        row_data = []
        for col in range(tableWidget.columnCount()):
            # Access data even from hidden columns
            item = tableWidget.item(row_index.row(), col)
            if item is not None:
                row_data.append(item.text())
            else:
                row_data.append(None)
        selected_data.append(row_data)

    return selected_data
