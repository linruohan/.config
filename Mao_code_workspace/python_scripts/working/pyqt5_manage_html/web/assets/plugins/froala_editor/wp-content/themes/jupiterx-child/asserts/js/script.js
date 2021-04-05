jQuery(document).ready(function ($) {

    /* Features Page */
    $("a[for='edit-mode']").on('click', function () {
        $(this).addClass('active-mode');
        $("a[for='design-mode']").removeClass('active-mode');
        $('#edit_block').addClass('active');
        $('#design_block').removeClass('active');
    });

    $("a[for='design-mode']").on('click', function () {
        $(this).addClass('active-mode');
        $("a[for='edit-mode']").removeClass('active-mode');
        $('#design_block').addClass('active');
        $('#edit_block').removeClass('active');
    });

    /* Pricing Page */
    $('#desktop-show-more-button').click(function () {
        if ($(this).children().hasClass('fa-minus')) {
            $('.more-features').css('display', 'none');
            $(this).find('.fa-minus').removeClass('fa-minus');
            $(this).children('i').addClass('fa-plus');
            $('#desktop-show-more-button p').html('More features').css('left', '-18px');
        } else {
            $('.more-features').css('display', 'table-row');
            $(this).find('.fa-plus').removeClass('fa-plus');
            $(this).children('i').addClass('fa-minus');
            $('#desktop-show-more-button p').html('Less features').css('left', '-18px');
        }
    });

    $('#jet-popup-5054').addClass('discount-modal');

    if (window.location.href.indexOf('/wysiwyg-editor/pricing/') > -1) {
        var pricingLsData = JSON.parse(localStorage.getItem('pricingJetPopupData'));
        if (pricingLsData && pricingLsData['status'] === 'disable') {
            $('.discount-modal').css('display', 'none');
            $('#discount-row').css('display', 'block');
        }
        setTimeout(function () {
            localStorage.setItem('pricingJetPopupData', JSON.stringify({ status: 'disable' }));
        }, 500);
    }

    if ($.cookie('hide-after-click') == 'yes') {
        $('#privacy-disclaimer').addClass('hide--first');
    }
    $('#agree-privacy').click(function () {
        if (!$('#privacy-disclaimer').is('hide--first')) {
            $('#privacy-disclaimer').addClass('hide--first');
            $.cookie('hide-after-click', 'yes', { expires: 150, path: '/' });
        }
        return false;
    });
});

(function ($) {

    /* Mailchimlp Form Validation Js Code */

    var validateEmptyForm = function ($form) {
            var valid = true;
            $form.find('.validate-empty:visible').each(function () {
                if (!validateEmpty(this)) {
                    valid = false;
                }
            });
            return valid;
        },
        validateEmpty = function (input) {
            var $input = $(input),
                $form_group = $input.parent(),
                $error_helper = $form_group.find('.error-helper'),
                valid = !($input.val() === '' || ($input.attr('type') === 'checkbox' && !$input.is(':checked')));

            if (valid && !!$error_helper.length && $error_helper.html().includes('blank')) {
                $form_group.removeClass('has-error');
            } else {
                $form_group.addClass('has-error');
                if (!!$error_helper.length) {
                    if ($input.attr('type') !== 'checkbox') {
                        $error_helper.html(($input.attr('placeholder') || '').replace(' *', '') + " can't be blank.");
                    } else {
                        $error_helper.html('The checkbox above is required.');
                    }
                }
            }
            return valid;
        },
        validateEmail = function (input) {
            var $input = $(input),
                $form_group = $input.parent(),
                $error_helper = $form_group.find('.error-helper'),
                valid = !($input.val() !== '' && !$input.val().match(/^([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})$/i));

            if (valid && !!$error_helper.length && $error_helper.html().includes('Email')) {
                $form_group.removeClass('has-error');
            } else {
                $form_group.addClass('has-error');
                if (!!$error_helper.length) {
                    $error_helper.html('Email is incorrect.');
                }
            }
            return valid;
        };

    /* Submit form */

    $(document)
        .on('ready', function () {
            $('#mc-embedded-subscribe-form').submit(function () {
                $('#sign-up').hide();
                $('#sign-up-done').show();
                return true;
            });

            $('#billing_country_code').trigger('change');

            $('.validate-email').blur(function () {
                return validateEmail(this);
            });

            $('.validate-empty').blur(function () {
                return validateEmpty(this);
            });
        })
        .on('click', 'form button[type="submit"], form input[type="submit"]', function (e) {
            var $form = $(this).parents('form');
            $form.find('.has-error:visible:first :input').focus();
            return validateEmptyForm($form);
        });
})(jQuery);
/* Script for Eloqua form */
function handleCountryChangepopup(element) {
    var country = $(element).val();
    console.log(country);

    if(country == "US" || country == "CA" || country == "BR" || country == "MX") {
        $(".state-block").css('display','block');
        if(country == "US") {
            jQuery(element.form).find("input[name=StateProvince]").val(jQuery(element.form).find("select[name=State]").val());
            jQuery(element.form).find(".state-block").css('display','block');
            jQuery(element.form).find(".us_privacy_policy").show();
            jQuery(element.form).find("select[name=State]").css('display','block');
            jQuery(element.form).find("select[name=Province]").hide();
            jQuery(element.form).find("select[name=BStates]").hide();
            jQuery(element.form).find("select[name=MStates]").hide();
            jQuery(element.form).find("select[name=State]").prop('required', true);
            jQuery(element.form).find("select[name=Province]").prop('required', false);
            jQuery(element.form).find("select[name=BStates]").prop('required', false);
            jQuery(element.form).find("select[name=MStates]").prop('required', false);

        }
        if (country == "CA"){
            console.log("sdsa");
            // debugger;
            jQuery(element.form).children("input[name=StateProvince]").val(jQuery(element.form).children("select[name=Province]").val());
            jQuery(element.form).find(".state-block").css('display','inline');
            jQuery(element.form).find(".us_privacy_policy").hide();
            jQuery(element.form).find("select[name=State]").hide();
            jQuery(element.form).find("select[name=Province]").css('display','inline');
            jQuery(element.form).find("select[name=BStates]").hide();
            jQuery(element.form).find("select[name=MStates]").hide();
            jQuery(element.form).find("select[name=State]").prop('required', false);
            jQuery(element.form).find("select[name=Province]").prop('required', true);
            jQuery(element.form).find("select[name=BStates]").prop('required', false);
            jQuery(element.form).find("select[name=MStates]").prop('required', false);
        }
        if (country == "BR"){ jQuery(element.form).find(".us_privacy_policy").hide();
            jQuery(element.form).find("input[name=StateProvince]").val($("select[name=BStates]").val());
            jQuery(element.form).find(".state-block").css('display','block');
            jQuery(element.form).find("select[name=State]").hide();
            jQuery(element.form).find("select[name=Province]").hide();
            jQuery(element.form).find("select[name=BStates]").css('display','block');
            jQuery(element.form).find("select[name=MStates]").hide();
            jQuery(element.form).find("select[name=State]").prop('required', false);
            jQuery(element.form).find("select[name=Province]").prop('required', false);
            jQuery(element.form).find("select[name=BStates]").prop('required', true);
            jQuery(element.form).find("select[name=MStates]").prop('required', false);
        }
        if (country == "MX"){ jQuery(element.form).find(".us_privacy_policy").hide();
            jQuery(element.form).find("input[name=StateProvince]").val($("select[name=MStates]").val());
            jQuery(element.form).find(".state-block").css('display','block');
            jQuery(element.form).find("select[name=State]").hide();
            jQuery(element.form).find("select[name=Province]").hide();
            jQuery(element.form).find("select[name=BStates]").hide();
            jQuery(element.form).find("select[name=MStates]").css('display','block');
            jQuery(element.form).find("select[name=State]").prop('required', false);
            jQuery(element.form).find("select[name=Province]").prop('required', false);
            jQuery(element.form).find("select[name=BStates]").prop('required', false);
            jQuery(element.form).find("select[name=MStates]").prop('required', true);
        }

    } else {
        jQuery(element.form).find(".us_privacy_policy").hide();
        jQuery(element.form).find("input[name=StateProvince]").val("");

        jQuery(element.form).find(".state-block").hide();
        jQuery(element.form).find("select[name=State]").prop('required', false);
        jQuery(element.form).find("select[name=Province]").prop('required', false);
        jQuery(element.form).find("select[name=BStates]").prop('required', false);
        jQuery(element.form).find("select[name=MStates]").prop('required', false);
    }

    if(country == "BE"  || country == "BG"  || country == "CZ"
        || country == "DK"  || country == "DE"  || country == "EE"
        || country == "IE"  || country == "GR"  || country == "ES"
        || country == "FR"  || country == "HR"  || country == "IT"
        || country == "CY"  || country == "LV"  || country == "LT"
        || country == "LU"  || country == "HU"  || country == "MT"
        || country == "NL"  || country == "AT"  || country == "PL"
        || country == "PT"  || country == "RO"  || country == "SI"
        || country == "SK"  || country == "FI"  || country == "SE"
        || country == "UK" || country == "CA" ) {
        jQuery(element.form).find(".gdpr-block").css('display','block');
        var checkbox = jQuery(element.form).find("input[name=TermsAndConditions]");
        checkbox.prop('required', true);
        var checkbox1 = jQuery(element.form).find("input[name=MarketingCommunications]");
        checkbox1.prop('required', true);
        jQuery(element.form).find(".casl-block").hide();
        var checkbox2 = jQuery(element.form).find("input[name=CanadaMarketingCommunications]");
        checkbox2.prop('required', false);
    }

    else {
        jQuery(element.form).find(".gdpr-block").hide();
        var checkbox = jQuery(element.form).find("input[name=TermsAndConditions]");
        checkbox.prop('required', false);
        var checkbox1 = jQuery(element.form).find("input[name=MarketingCommunications]");
        checkbox1.prop('required', false);
        jQuery(element.form).find(".casl-block").hide();
        var checkbox2 = jQuery(element.form).find("input[name=CanadaMarketingCommunications]");
        checkbox2.prop('required', false);

    }
}
//});
function handleStateChangetest(element) {
    var state = $(element).val();
    console.log("statechange");
    jQuery(element.form).find("input[name=stateProv]").val(state);

}
$(document).ready(function() {
    jQuery('#mc-embedded-subscribe').click(function(event) {
        event.preventDefault();
        jQuery('#signupModal').show();

    });
    jQuery('.jupiterx-footer #mc-embedded-subscribe').click(function(event) {
        event.preventDefault();
        jQuery('#signupModal').show();

    });
    var options = {
        //target:        '#output2',   // target element(s) to be updated with server response
        beforeSubmit:  showRequest,  // pre-submit callback
        success:       showResponse,  // post-submit callback

        // other available options:
        url:       'https://s608.t.eloqua.com/e/f2'         // override for form's 'action' attribute
        //type:      type        // 'get' or 'post', override for form's 'method' attribute
        //dataType:  null        // 'xml', 'script', or 'json' (expected server response type)
        //clearForm: true        // clear all form fields after successful submit
        //resetForm: true        // reset the form after successful submit

        // $.ajax options can be used here too, for example:
        //timeout:   3000
    };

    // bind to the form's submit event
    $('#form3411').submit(function() {
        // inside event callbacks 'this' is the DOM element so we first
        // wrap it in a jQuery object and then invoke ajaxSubmit

        $(this).ajaxSubmit(options);

        // !!! Important !!!
        // always return false to prevent standard browser submit and page navigation
        return false;
    });
});

// pre-submit callback
function showRequest(formData, jqForm, options) {

    // formData is an array; here we use $.param to convert it to a string to display it
    // but the form plugin does this for you automatically when it submits the data
    jQuery('.message_elq').show();
    formData[formData.length] = { "name": "elqFormName", "value": "FRONewsSubscription" };
    formData[formData.length] = { "name": "elqSiteId", "value": "608" };
    formData[formData.length] = { "name": "Topic", "value": "FROeditor" };
    var queryString = $.param(formData);

    // jqForm is a jQuery object encapsulating the form element.  To access the
    // DOM element for the form do this:
    // var formElement = jqForm[0];

    //alert('About to submit: \n\n' + queryString);

    // here we could return false to prevent the form from being submitted;
    // returning anything other than false will allow the form submit to continue
    return true;
}

// post-submit callback
function showResponse(responseText, statusText, xhr, $form)  {
    // for normal html responses, the first argument to the success callback
    // is the XMLHttpRequest object's responseText property

    // if the ajaxSubmit method was passed an Options Object with the dataType
    // property set to 'xml' then the first argument to the success callback
    // is the XMLHttpRequest object's responseXML property

    // if the ajaxSubmit method was passed an Options Object with the dataType
    // property set to 'json' then the first argument to the success callback
    // is the json data object returned by the server
    console.log(responseText);
    console.log("statusText-"+statusText);
    if(statusText=='success'){
        jQuery('.message_elq').html('Thanks for subscribeing us. You will be redirected');
        if(jQuery(location).attr("href")=='https://froala.com/'){
            jQuery('.message_elq').html('Thanks for subscribing us.');
            jQuery('#signupModal').fadeOut(600);
        }else{
            window.location.replace('https://froala.com/');
        }

    }
    //alert('status: ' + statusText + '\n\nresponseText: \n' + responseText +
    //'\n\nThe output div should have already been updated with the responseText.');
}
/* Script for Eloqua form */