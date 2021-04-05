function getCookieValue(cname) { // cname is nothing but the cookie value which
    //contains the value
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
jQuery(document).ready(function() {
    var utmsession=getCookieValue("UTMSession");
    var utmsessionArray = utmsession.split('&');
    if (jQuery("#utm_source").length > 0 && utmsessionArray[0].split("=")){
        jQuery("#utm_source").val(utmsessionArray[0].split("=")[1]);
    }
    if (jQuery("#utm_content").length > 0 && utmsessionArray[1].split("=")){
        jQuery("#utm_content").val(utmsessionArray[1].split("=")[1]);
    }
    if (jQuery("#utm_campaign").length > 0 && utmsessionArray[2].split("=")){
        jQuery("#utm_campaign").val(utmsessionArray[2].split("=")[1]);
    }
    if (jQuery("#utm_term").length > 0 && utmsessionArray[3].split("=")){
        jQuery("#utm_term").val(utmsessionArray[3].split("=")[1]);
    }
    if (jQuery("#utm_medium").length > 0 && utmsessionArray[4].split("=")){
        jQuery("#utm_medium").val(utmsessionArray[4].split("=")[1]);
    }
});