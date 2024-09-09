$(document).ready(function () {
  //display speak message
  eel.expose(DisplayMessage);
  function DisplayMessage(message) {
    $(".siri-message li:first").text(message);
    $(".siri-message").textillate("start");
  }

  //display hood
  eel.expose(ShowHood);
  function ShowHood() {
    $("#Oval").attr("hidden", false);
    $("#SiriWave").attr("hidden", true);
  }

  eel.expose(senderText);
  function senderText(message) {
    var chatBox = document.getElementById("offcanvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `<div class="row justify-content-end mb-4">
        <div class="width-size">
        <div class="sender_message">${message}</div>`;
      //scroll to the bottom of chatbox
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }
  eel.expose(recieverText);
  function recieverText(message) {
    var chatBox = document.getElementById("offcanvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `<div class="row justify-content-start mb-4">
        <div class="width-size">
        <div class="reciever_message">${message}</div>`;
      //scroll to the bottom of chatbox
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }
});
