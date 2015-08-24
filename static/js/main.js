!function(a){"use strict";a(function(){var b=a(window),c=a(document.body);c.scrollspy({target:".sidebar"}),b.on("load",function(){c.scrollspy("refresh")}),a(".bs-docs-container [href=#]").click(function(a){a.preventDefault()}),setTimeout(function(){var b=a(".sidebar");b.affix({offset:{top:function(){var c=b.offset().top,d=parseInt(b.children(0).css("margin-top"),10),e=a(".bs-docs-nav").height();return this.top=c-e-d},bottom:function(){return this.bottom=a(".bs-docs-footer")}}})},100);})}(jQuery);



$(function(){
    var sea_service = $(".sea-service-button");
    var d = new Date();
    var month = d.getMonth()+1;
    var day = d.getDate();
    var date = ((''+month).length<2 ? '0' : '') + month + '/' +
        ((''+day).length<2 ? '0' : '') + day + '/' + d.getFullYear(); 
    var x = ''; 
    count = 0;
    // full name in the bottom most of the code
    var full_name = function(){
                      last_name = $("#last_name").val();
                      first_name = $("#first_name").val();
                      middle_name = $("#middle_name").val();
                      full_name = $("#full_name").val(first_name+' '+middle_name+' '+last_name);
                    };

    // auto title tooltip if text is typed
    var tooltip = function(){
                    val = $(this).val();
                    if(val == ''){
                      $(this).attr("title", "");
                      $(this).attr("data-original-title", "");
                    }else{
                      placeholder = $(this).attr("placeholder");
                      $(this).attr("title", placeholder);
                      $(this).attr("data-original-title", placeholder);
                    }
                  };

    // same affress function
    var address = function(){
        permanent_street = $("#permanent_street").val();
        permanent_town = $("#permanent_town").val();
        permanent_baranggay = $("#permanent_baranggay").val();
        permanent_municipality = $("#permanent_municipality").val();
        permanent_zip = $("#permanent_zip").val();
        current_street = $("#current_street").val();
        current_town = $("#current_town").val();
        current_baranggay = $("#current_baranggay").val();
        current_municipality = $("#current_municipality").val();
        current_zip = $("#current_zip").val();
        if(permanent_street == current_street && 
            permanent_town == current_town && 
            permanent_baranggay == current_baranggay &&
            permanent_municipality == current_municipality && 
            permanent_zip == current_zip){
          $("#same_address").prop("checked", true);
        }else{
          $("#same_address").prop("checked", false);
        }
    };         

    var autocomplete = function(){

    }

    // 50 words essay word count validation
    var essay = function(event){
      var _essay = document.getElementById('essay');
      try{
        essay = _essay.value.match(/\S+/g).length;
      }
      catch(err){
        return false;
      }
      if(essay < 50){
        _essay.setCustomValidity('Please answer the essay with a minimum of fifty words');
        
      }else{
        _essay.setCustomValidity('');
      }
      $('#display_count').text(essay);
    }

    var tertiary = [      
      "PMI", 
      "PMMA",
      "JBLFU",
      "MAAP",
      "TIP", 
    ];
    var degree = [      
      "BSMARE", 
      "BSMT",
      "EE",
      "ECE",
      "COE", 
    ];
    var vtype = [
      "Bulk",
      "Oil Tanker",
      "Chem Tanker",
    ];
    var flag = [
      "Caymen Islands",
      "Marshall Islands",
      "Liberia",
      "Cyprus",
      "Singapore",
      "Greek",
    ];
    var manning_agency = [
      "ACE NAVIGATION COMPANY INC",
      "BAN-UDEN CREWING INC",
      "CAPITAL SHIPMANNING PHILS INC",
      "DELFI SHIPPING AGENCY INC",
      "EAGLE CLARC SHIPPING PHILIPPINES INC",
      "OSTE CREWING PHILIPPINES INC",
    ];
    var rank = [
      "Captain",
      "Chief Mate",
      "Chief Engineer",
      "2nd Engineer",
    ];


    $("input[name='visa_entry']").change(function(){
      html = ''
      val = $(this).val();
      if(val=='yes'){
        html = "<textarea class='form-control'></textarea>";
      }
      $("p#visa_entry_yes").html(html);
    });
    $("input[name='leave_order']").change(function(){
      html = ''
      val = $(this).val();
      if(val=='yes'){
        html = "<textarea class='form-control'></textarea>";
      }
      $("p#leave_order_yes").html(html);
    });
    $("input[name='disciplinary_action']").change(function(){
      html = ''
      val = $(this).val();
      if(val=='yes'){
        html = "<textarea class='form-control'></textarea>";
      }
      $("p#disciplinary_action_yes").html(html);
    });
    $("input[name='source']").click(function(){
      val = $(this).val();
      if($(this).is(':checked') && val != 'seafarer_center'){
        $('.specific').remove();
        if(val == 'internet'){ 
          label = '<label class="specific"><b>(Website Name/Address)</b></label>';
        }else{
          label = '<label class="specific"><b>(Please Specify)</b></label>';
        }
        $(this).parent().append(label+" <input type='text' class='specific' name='specific'>");
      }else{
        $(this).parent().children("label, input[type='text']").remove();
      }
    });
    $(".ecdis-specific").change(function(){
      val = $(this).val();
      if($(this).is(':checked')){
          label = '<label>(Please specify brand): </label>';
          $(this).parent().append(label+" <input type='text'>");
        }
      else{
        $(this).parent().children("label, input[type='text']").remove();
      }
    });
    $("#same_address").change(function(){
      if($(this).is(':checked')){
        street = $("#permanent_street").val();
        town = $("#permanent_town").val();
        baranggay = $("#permanent_baranggay").val();
        municipality = $("#permanent_municipality").val();
        zip = $("#permanent_zip").val();
        if(municipality != 'Municipality'){
          $("#current_municipality").css("color", "#000");
        }
        if(town != 'Town'){
          $("#current_town").css("color", "#000");
        }
      }else{
        street = "";
        town = "Town";
        baranggay = "";
        municipality = "Municipality";
        zip = "";
      }
      $("#current_street").val(street);
      $("#current_town").val(town);
      $("#current_baranggay").val(baranggay);
      $("#current_municipality").val(municipality);
      $("#current_zip").val(zip);
    });


    $("tbody").on("click", ".add-row", function(){
      html = $(".first-row").html();
      $(this).parent().parent().after("<tr>"+html+"</tr>");
    });
    $("tbody").on("click", ".delete-row", function(){
      $(this).parent().parent().remove();
    });
    $("body").on("focus", ".date", function(){
      $(this).datepicker({ 
        changeYear: true, 
        changeMonth: true, 
        yearRange: "1950:"+d.getFullYear(), 
        showButtonPanel: true,
        closeText: 'Clear',
        beforeShow: function (e, t) {
          $("#ui-datepicker-div").addClass('HideTodayButton');
        },
        onClose: function () {
          var event = arguments.callee.caller.caller.arguments[0];
          if ($(event.delegateTarget).hasClass('ui-datepicker-close')) {
            $(this).val('');
          }
          if($(this).hasClass('date-joined') || $(this).hasClass('date-left')){
            val = $(this).val();
            date_val = new Date(val);
            // val2 is used to get the day after the day selected 
            val2 = new Date();
            val2.setDate(date_val.getDate() + 1);
            duration = $(this).parent().siblings("td").find(".duration");
            if($(this).hasClass('date-joined')){
              _date_left = $(this).parent().next("td").children();
              date_left = new Date(_date_left.val());
              if(val == ''){
                _date_left.prop("disabled", true);
              }else{
                _date_left.prop("disabled", false);
                setTimeout(function(){ _date_left.focus(); }, 1000);
                setTimeout(function(){ $(this).datepicker("show"); }, 1000);
              }
              // _date_left.datepicker({ minDate: val2   });
              // var minDate = _date_left.datepicker( "option", "minDate");
              // _date_left.datepicker("option", "minDate", val2);
              _date_left.val("");
              duration.val("");
            }else if($(this).hasClass('date-left')){
              date_joined = $(this).parent().prev("td").children().val();
              date_joined = new Date(date_joined);
              
              if( date_joined != '' ){
                total_duration = Math.abs(date_joined.getTime() - date_val.getTime());
                total_duration = Math.ceil(total_duration / (1000 * 3600 * 24));
              }
              if( total_duration ){
                duration.val(total_duration);
              }
            }
          }
        }
      });
    }).on("keydown", ".date", function(e){
      // prevents erasing via backspace
      if (e.which === 8) {
            e.preventDefault();
      }
    });
    $('.sidebar').on('activate.bs.scrollspy', function () {
      // boolean is used for the sea-service to pop-up only from top to bottom
      if ($(this).find("li.active").text().trim() == 'Emergency Contact Details'){
        x = 1;
      }if($(this).find("li.active").text().trim() == 'Background Information'){
        x = 0;
      }
      if ($(this).find("li.active").text().trim() == 'Sea Service' && x == 1){
        $(sea_service).click();
      }
    });
    $.fn.modal.Constructor.prototype.enforceFocus = function () { };

    $(".month-only").datepicker({ 
      showButtonPanel: true,
      changeYear: false,  
      dateFormat: 'mm-yy',
      beforeShow: function (e, t) {
        $("#ui-datepicker-div").addClass("hide-calendar");
        $("#ui-datepicker-div").addClass('HideTodayButton');
      },
      onClose: function(dateText, inst){
        var n = Math.abs($("#ui-datepicker-div .ui-datepicker-month :selected").val() - 1) + 2;
        $(this).datepicker("setDate", new Date(null, n, null));
        setTimeout(function(){ $("#ui-datepicker-div").removeClass("hide-calendar"); }, 300);
        setTimeout(function(){ $("#ui-datepicker-div").removeClass('HideTodayButton'); }, 300);
      }
    });


    $('.application-date').val(date);
    $('[data-toggle="tooltip"]').tooltip({ html: true });
    $("input[type='text']").keyup(tooltip).click(full_name).focusout(full_name);
    $("#last_name, #first_name, #middle_name").keyup(full_name).click(full_name).focusout(full_name);
    $("#permanent_street, #permanent_town, #permanent_baranggay, #permanent_municipality, #permanent_zip, #current_street, #current_town, #current_baranggay, #current_municipality, #current_zip").keyup(address).change(address);
    $(".essay").keyup(essay).click(essay).focusout(essay);
    $(".sea-services input").keyup(function(){
      $(this).parent().siblings().children().prop("required", "true");
    });
    // Sea Service Validation
    $("#proceed-sea-service").click(function(){
      $('.sea-services').find('input').each(function(){
        if($(this).prop('required') && $(this).next('ul').length != 1 && $(this).val().length < 1){
          count++;
          $(this).after("<ul class='errorlist'><li>This field is required.</li></ul>");
        }else if($(this).val().length >= 1 && $(this).next('ul').length == 1){
          count--;
          $(this).next('ul').remove();
        }
      });
      $('.sea-services').find('select').each(function(){
        if($(this).prop('required') && $(this).next('ul').length != 1 && $(this).val() == "Cause of Discharge"){
          count++;
          $(this).after("<ul class='errorlist'><li>This field is required.</li></ul>");
        }else if($(this).val() != "Cause of Discharge" && $(this).next('ul').length == 1){
          count--;
          $(this).next('ul').remove();
        }
      });
      setTimeout(function(){ 
        // alert(count); 
        if(count == 0){ 
          // closes the modal 
          $('#seaservice').modal('hide');
          $('h5.validations').text("");
        }else{
          $('h5.validations').text(count+ " REQUIRED FIELDS NEED TO BE FILLED UP");
        } 
      }, 500);
    });
    $(".essay").trigger('click');
    $("body").on("change", "select", function(){
      val = $(this).val();
      $(this).css("color", "#000");
    });

    $("#tertiary").autocomplete({
      source: function(request, response){
        var results = $.ui.autocomplete.filter(tertiary, request.term);
        response(results.slice(0, 10));
      }
    });
    $("#degree").autocomplete({
      source: function(request, response){
        var results = $.ui.autocomplete.filter(degree, request.term);
        response(results.slice(0, 10));
      }
    });
    $("body").on("focus", ".vtype", function(){
      $(this).autocomplete({
        source: function(request, response){
          var results = $.ui.autocomplete.filter(vtype, request.term);
          response(results.slice(0, 10));
        }
      });
    });
    $("body").on("focus", ".flag", function(){
      $(this).autocomplete({
        source: function(request, response){
          var results = $.ui.autocomplete.filter(flag, request.term);
          response(results.slice(0, 10));
        }
      });
    });
    $("body").on("focus", ".manning_agency", function(){
      $(this).autocomplete({
        source: function(request, response){
          var results = $.ui.autocomplete.filter(manning_agency, request.term);
          response(results.slice(0, 10));
        }
      });
    });
    $("body").on("focus", ".rank", function(){
      $(this).autocomplete({
        source: function(request, response){
          var results = $.ui.autocomplete.filter(rank, request.term);
          response(results.slice(0, 10));
        }
      });
    });
    // Enables the signature on the modal
    $('#signature').on('show.bs.modal', function (e){
      $(".jSignature").jSignature();
      $(".jSignature").resize();
    });

    // Auto Age
    $(".birth_date").change(function(){
      val = $(this).val();
      var birthday = new Date(val);
      var today = new Date();
      var age = ((today - birthday) / (31557600000));
      var age = Math.floor( age );
      $(".age").val(age);
    });
    $(".search-zip").click(function(){
      params = $(this).attr('data-params');
      permanent_baranggay = $("#"+params+"_baranggay").val();
      permanent_zip = $("#"+params+"_zip").val();
      permanent_municipality = $("#"+params+"_municipality").val();
      permanent_town = $("#"+params+"_town").val();
      permanent_street = $("#"+params+"_street").val();
      permanent_address = permanent_baranggay+"+"+permanent_municipality+"+"+"zip code";
      permanent_address = permanent_address.replace(/ /g,"+");
      var myWindow = window.open("http://www.google.com.ph/#q="+permanent_address, "", "width=1000, height=700");
    });
    
    if($("#id_alternative_position").val() != "Alternative Position"){
      $("#id_alternative_position").css("color", "#000");
    }
    if($("#id_position_applied").val() != "Position Applied"){
      $("#id_position_applied").css("color", "#000");
    }    
}); 