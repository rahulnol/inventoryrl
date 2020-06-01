function mySignUpBtn() {
    userName = $('#signinSrUsername').val()
    phoneNo = $('#signinSrPhoneno').val()
    email = $('#signinSrEmail').val()
    password = $('#signinSrPassword').val()
    cpassword = $('#signinSrConfirmPassword').val()
    cbterm = false
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    if ($('#termsCheckbox').prop("checked") == true) {
        cbterm = true;
    } else {
        cbterm = false;
    }
    $('#myErrorDivResUsername').hide();
    $('#myErrorDivResEmail').hide();
    $('#myErrorDivResPhoneno').hide();


    $('#myErrorDivUsername').hide();
    $('#myErrorDivPhoneno').hide();
    $('#myErrorDivEmail').hide();
    $('#myErrorDivPassword').hide();
    $('#myErrorDivConfirmPassword').hide();
    $('#myErrorDivCheckBox').hide();

    var error = false;
    if (!userName || userName.length < 3) {
        $('#myErrorDivUsername').show();
        error = true;
    }

    if (!phoneNo || phoneNo.length != 10) {
        $('#myErrorDivPhoneno').show();
        error = true;
    }

    if (!email.match(mailformat)) {
        $('#myErrorDivEmail').show();
        error = true;
    }

    if (password != cpassword || !password || !cpassword) {
        $('#myErrorDivConfirmPassword').show();
        error = true;
    }
    if (!cbterm) {
        $("#mySignupFormId").submit(function (e) {
            e.preventDefault();
            $('#myErrorDivCheckBox').show();

        });
        error = true;
    } else {
        $("#mySignupFormId").submit(function (e) {
            e.preventDefault();
            $('#myErrorDivCheckBox').hide();
        });
    }
    if (error) {
        return;

    } else {
        $.ajax({
            url: 'http://127.0.0.1:8000/',
            type: 'POST',
            data: JSON.stringify({
                'jsuname': userName,
                'jsphoneno': phoneNo,
                'jsemail': email,
                'jspassword': password
            }),
            success: function (data, n) {
                if (data.mysuccess == 'Fail') {
                    $('#success-div').hide();
                    $('#myErrorDivResUsername').text(data.mymsguname || '').show();
                    $('#myErrorDivResEmail').text(data.mymsgemail || '').show();
                    $('#myErrorDivResPhoneno').text(data.mymsgphone || '').show();
                }
                if (data.mysuccess == 'Pass') {
                    $('#success-div').text(data.mymsg).show();
                    window.location.href=data.myurl;
                }
            },
            error: function (a, b) {
                console.log('a : ',a)
                console.log('b : ',b)


            }
        })
    }

}