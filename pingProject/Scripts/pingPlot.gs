function pingGraph() {
  var mainSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("main");

  var newOfflineRow = find("New offline today:");
  var newOnlineRow = find("Back online today:");

  var today = mainSheet.getRange(1,2).getValue().split("|")[1];
  var formToday = today.substring(1, today.length-1);
  Logger.log(formToday);

  var totalOffline = mainSheet.getRange(1, 3).getValue();
  var newOffline = mainSheet.getRange(newOfflineRow, 3).getValue();
  var newOnline = mainSheet.getRange(newOnlineRow, 3).getValue();

  var historySheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("history");

  var newRow = [formToday, totalOffline, newOffline, newOnline];
  historySheet.appendRow(newRow)



var series = {
  0: {
    dataLabel: "value"
  }
};
  var chart = mainSheet.newChart()
    .setChartType(Charts.ChartType.LINE)
    .addRange(historySheet.getRange("A1:D500")).setNumHeaders(1)
    .setPosition(5, 5, 0, 0)
    .setOption("title","Comms stats")
    .setOption("legend", {position: "top"})
    .build();

mainSheet.insertChart(chart);

function find(item) {

  var listRows = mainSheet.getDataRange().getValues();
   for (var i =0;i<listRows.length;i++)
   {
    if (listRows[i][1] == item)
       {

           return i+1;
       }
   }
  }
}

