function my_message(){
    var content = 'None'
    var un = document.getElementById('un').innerText
    var pw = document.getElementById('pw').innerText
    var cur = document.getElementById('cur').innerText
    content = "<ul>"
            +"<li>"
            +"Username: "
            +un
            +"</li>"
            +"<li>"
            +"Password: "
            +pw
            +"</li>"
            +"<li>"
            +"Your Currency: "
            +cur
            +"</li>"
            +"</ul>"
    Swal.fire({
        title: '<strong>Your message</strong>',
        type: 'info',
        html: content,
        focusConfirm: true,
        showCloseButton: true,
    })
}

function contact() {
    Swal.fire(
        title = "Contact us by this:",
        text = "QQ email:3211761626@qq.com cellphone:183-8213-4336",
        type =  "question"
    )
}

function chane(){
    alert("Successful change!")
}