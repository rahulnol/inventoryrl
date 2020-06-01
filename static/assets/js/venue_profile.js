$('#miCheckIconEditVenueDesc').click(function () {
    var venueDesc = $('#miTextAreaEditDiv').val();
    var venueId = $('#miVenueId').val();
    if (venueDesc.length < 20) {
        $('#miErrorDivForTextArea').show();
    } else {
        $('#miErrorDivForTextArea').hide();
        myData = {
            'jsVenueId':venueId,
            'jsVenueDesc':venueDesc,
            'myCheck':'DescEditPutCall'

        }
        $.ajax({
            url: 'http://127.0.0.1:8000/venue/profile/',
            type: 'PUT',
            data: JSON.stringify(myData),
            success: function (data,status) {
                if(data.success == 'Pass'){
                    window.location.reload();
                }
                if(data.success == 'Fail'){
                    
                }
            },
            error: function (data,status) {
                
            }

        })

    }
})

$('#miEditIconVenueDesc').click(function () {
    $('#miOriginalVenueDescDiv').hide();
    $('#miVenueDescEditDiv').show();
    var jsVenueDesc = $(this).parent().data('venuedesc');
    var jsVenueId = $(this).parent().data('venueid');
    $('#miTextAreaEditDiv').val(jsVenueDesc);
    $('#miVenueId').val(jsVenueId);

});

$('#miCrossIconEditVenueDesc').click(function () {
    $('#miOriginalVenueDescDiv').show();
    $('#miVenueDescEditDiv').hide();
});


$('#miEditIconContactInfo').click(function () {
    $('#miContactInfoModal').modal('show');
    $('#miDivEmailError').hide();
    $('#miDivPhoneError').hide();
    $('#miDivLandmarkError').hide();
    $('#miDivWebsiteError').hide();
    $('#miErrorDivResponse').hide();
    var venue = $(this).parent().data('venue');
    $('#miInputEmail').val(venue.email);
    $('#miInputPhone').val(venue.phone);
    $('#miInputLandLine').val(venue.landline);
    $('#miInputLandmark').val(venue.landmark);
    $('#miInputWebsite').val(venue.website);
    $('#miVenueId').val(venue.id);
})

$('#miContactInfoModal #miSaveBtnContactInfoModal').click(function () {
    var jsEmail = $('#miInputEmail').val();
    var jsPhone = $('#miInputPhone').val();
    var jsLandLine = $('#miInputLandLine').val();
    var jsLandmark = $('#miInputLandmark').val();
    var jsWebsite = $('#miInputWebsite').val();
    var jsVenueId = $('#miVenueId').val();

    myError = false;
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (!jsEmail.match(mailformat)) {
        $('#miDivEmailError').show();
        myError = true;
    } else {
        $('#miDivEmailError').hide();
    }

    if (jsPhone.length < 10 || jsPhone.length > 10) {
        $('#miDivPhoneError').show();
        myError = true;
    } else {
        $('#miDivPhoneError').hide();
    }

    if (jsLandLine.length < 11 || jsLandLine.length > 11) {
        jsLandLine = '02746277677';
    } else {
        jsLandLine = $('#miInputLandLine').val();

    }
    if (!jsLandmark) {
        $('#miDivLandmarkError').show();
        myError = true;
    } else {
        $('#miDivLandmarkError').hide();
    }

    if (!jsWebsite) {
        $('#miDivWebsiteError').show();
        myError = true;
    } else {
        $('#miDivWebsiteError').hide();
    }
    if (myError) {
        return;
    } else {
        $('#miDivEmailError').hide();
        $('#miDivPhoneError').hide();
        $('#miDivLandmarkError').hide();
        $('#miDivWebsiteError').hide();

        myData = {
            'jsEmail': jsEmail,
            'jsPhone': jsPhone,
            'jsLandline': jsLandLine,
            'jsLandmark': jsLandmark,
            'jsWebsite': jsWebsite,
            'jsVenueId': jsVenueId,
            'myCheck':'ContactInfoPutCall'
            //'jsVenueId':23
        }
        $.ajax({
            url: 'http://127.0.0.1:8000/venue/profile/',
            type: 'PUT',
            data: JSON.stringify(myData),
            success: function (data, status) {
                if (data.success == 'Fail') {
                    $('#miErrorDivResponse').show();
                } else {
                    window.location.reload();
                }

            }
        });
        //alert(jsEmail + '------' + jsPhone + '-------' + jsLandLine + '------' + jsLandmark + '----' + jsWebsite);
    }
})

$('#addSpaceBtn').click(function () {
    $('#spaceeditmodal').modal('show');
    $('#space_modal_save_btn').addClass('addSpaceBtn').removeClass('editSpaceBtn');
})

$(document).on('click', '.addSpaceBtn', function () {
    var spaceName = $('#spaceName').val();
    var venueId = document.getElementById("space_modal_select").value;
    var myError = false;
    if (!spaceName) {
        $('#errorSpan').show();
        myError = true;
    }
    if (!venueId) {
        $('#errorSpan').show();
        myError = true;
    }
    if (myError) {
        return;
    } else {
        $('#errorSpan').hide();
        $.ajax({
            url: 'http://127.0.0.1:8000/venue/modifyspace/',
            type: 'POST',
            data: JSON.stringify({
                'spaceName': spaceName,
                'venueId': venueId,
            }),
            success: function (data, status) {
                if (data.success == 'Pass') {
                    window.location.reload()
                } else {
                }


            },
            error: function (data, status) {

            }
        })
    }
})

$(document).on('click', '.editSpaceBtn', function () {
    var spaceName = $('#spaceName').val();
    var spaceId = $('#space_id').val();
    var venue = $(this).parent().data('venue');
    //alert(venue.venue_name+'----'+venue.description+'---------------'+venue.contact_info);
    $.ajax({
        url: 'http://127.0.0.1:8000/venue/modifyspace/' + spaceId + '/',
        type: 'PUT',
        data: JSON.stringify({
            'jsspaceName': spaceName,
            'jsspaceId': spaceId,
            'jsvenueId': venue.id,
            'jsvenue': venue

        }),
        success: function (data, status) {
            var success = data.success;
            if (success == 'Pass') {
                window.location.reload();
            } else {
                alert(data.msg);
            }


        },
        error: function (data, status) {
        }

    })

})

// $('#space_modal_save_btn').click(function () {
//     var spaceName = $('#spaceName').val();
//     var spaceId = $('#space_id').val();
//     var venue = $(this).parent().data('venue');
//     //alert(venue.venue_name+'----'+venue.description+'---------------'+venue.contact_info);
//     $.ajax({
//         url: 'http://127.0.0.1:8000/venue/modifyspace/' + spaceId + '/',
//         type: 'PUT',
//         data: JSON.stringify({
//             'jsspaceName': spaceName,
//             'jsspaceId': spaceId,
//             'jsvenueId': venue.id,
//             'jsvenue': venue
//
//         }),
//         success: function (data, status) {
//             var success = data.success;
//             if (success == 'Pass') {
//                 window.location.reload();
//             } else {
//                 alert(data.msg);
//             }
//
//
//         },
//         error: function (data, status) {
//         }
//
//     })
//
// })


$('.space_edit_icon').click(function () {
    $('#spaceeditmodal').modal('show');
    $('#space_modal_save_btn').addClass('editSpaceBtn').removeClass('addSpaceBtn');
    var space = $(this).parent().data('space');
    $('#spaceName').val(space.name);
    $('#space_id').val(space.id);
})


$('.space_del_icon').click(function () {
    $('#deleteConfirmModal #content_type').html('Space');
    var space = $(this).parent().data('space');
    $('#deleteConfirmModal .btn-primary').attr('data-rid', space.id);
    $('#deleteConfirmModal .btn-primary').addClass('space_extra_class').removeClass('addon_delete_confirm');
    $('#deleteConfirmModal').modal('show');
})

$(document).on('click', '.space_extra_class', function () {
    var id = $(this).attr('data-rid');
    $.ajax({
        url: 'http://127.0.0.1:8000/venue/modifyspace/' + id + '/',
        type: 'DELETE',
        success: function (data, status) {
            window.location.reload();
        }
    })
});

$('#add_addon_btn').click(function () {
    $('#addonModal input[type="text"]').each(function () {
        $(this).val('');
    });
    $('#addonModal select').each(function () {
        $(this).val('');
    });

    $('#addonModal').modal('show');
});

$('#addon_save').click(function () {
    var name = $('#addon_item_name').val();
    var addon_quantity = $('#addon_quantity').val();
    var addon_price = $('#addon_price').val();
    var addon_sport = $('#addon_sport').val();
    var addon_id = $('#addon_id').val();
    if (!(name && addon_quantity && addon_sport && addon_price)) {
        $('#addonModal').find('.error').show();
        return;
    }
    var form_data = {
        'name': name,
        'quantity': addon_quantity,
        'price': addon_price,
        'sport_info_id': addon_sport,
    };
    if (addon_id) {
        var URL = 'http://127.0.0.1:8000/sports/addon/' + addon_id;
        var type = 'PUT';
        var data = JSON.stringify(form_data);
    } else {
        var URL = 'http://127.0.0.1:8000/sports/addon/';
        var type = 'POST';
        var data = form_data;
    }
    $.ajax({
        url: URL,
        type: type,
        data: data,
        success: function (data, status) {
            window.location.reload();
        }
    })
});

$('.addon_edit').click(function () {
    var object = $(this).parent().parent().data('object');
    $('#addon_item_name').val(object.name);
    $('#addon_quantity').val(object.count);
    $('#addon_price').val(object.hourly_price);
    $('#addon_sport').val(object.sport);
    $('#addon_id').val(object.id);
    $('#addonModal').modal('show');
});

$('.addon_delete').click(function () {
    $('#deleteConfirmModal #content_type').html('Addon');
    var object = $(this).parent().parent().data('object');
    $('#deleteConfirmModal .btn-primary').attr('data-id', object.id);
    $('#deleteConfirmModal .btn-primary').removeClass('space_extra_class').addClass('addon_delete_confirm');
    $('#deleteConfirmModal').modal('show');
})

$(document).on('click', '.addon_delete_confirm', function () {
    var id = $(this).attr('data-id');
    $.ajax({
        url: 'http://127.0.0.1:8000/sports/addon/' + id,
        type: 'DELETE',
        success: function (data, status) {
            var msg = data.msg;
            console.log(msg);
            window.location.reload();
        }
    })
});