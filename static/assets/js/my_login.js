function loginButton() {
    var error = false;
    jsemail = $('#signinSrEmail').val()
    jspassword = $('#signinSrPassword').val()

    if(!jsemail){
        $('#myErrorEmail').show()
        error = true;
    }

    if(!jspassword){
        $('#myErrorPassword').show()
        error = true
    }
    $('#myFormId').submit(function (e) {
            e.preventDefault();

        });

    if(error){
        return;
    }else{
        $.ajax({
            url: 'http://127.0.0.1:8000/validatelogin/',
            type: 'POST',
            data: JSON.stringify({
                'jsemail':jsemail,
                'jspasword':jspassword
            }),
            success: function (data,status) {
                if (data.mysuccess == 'Pass') {
                    $('#success-div').text(data.mymsg).show();
                    window.location.href=data.myurl;
                } else {
                    $('#login_error').show();
                }
            },
            error: function (data,status) {
                
            }
        })
    }


}