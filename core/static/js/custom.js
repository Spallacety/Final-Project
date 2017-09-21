import axios from 'axios';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "XCSRF-TOKEN";

$(document).ready(function() {
  $('.tooltipped').tooltip({delay: 50});
  $(".button-collapse").sideNav();
  $('.modal').modal({
    dismissible: true
  });
  $('select').material_select();
  $(".dropdown-button").dropdown({
    inDuration: 300,
    outDuration: 225,
    constrainWidth: false,
    hover: false,
    gutter: 0,
    belowOrigin: true,
    alignment: 'left',
    stopPropagation: false
  });
});