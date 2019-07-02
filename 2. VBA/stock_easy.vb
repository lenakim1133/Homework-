Sub easy()

Dim ws As Worksheet
Dim starting_ws As Worksheet
Set starting_ws = ActiveSheet

For Each ws In ThisWorkbook.Worksheets
ws.Activate

Dim ticker As String
Dim total_volume As Double
total_volume = 0
Dim total_table_row As Long

summary_table_row = 2

Dim i As Long

lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row



For i = 2 To lastrow

If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
ticker = Cells(i, 1).Value
total_volume = total_volume + Cells(i, 7).Value

Range("i" & summary_table_row).Value = ticker

Range("j" & summary_table_row).Value = total_volume

summary_table_row = total_table_row + 1

total_volume = 0

Else
total_volume = total_volume + Cells(i, 7).Value

End If

Next i

ws.Range("i1").Value = "Ticker"
ws.Range("j1").Value = "Total Stock Volume"

starting_ws.Activate


End Sub



