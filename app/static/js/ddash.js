$( document ).ready(function() {

    var socket = io.connect('http://' + document.domain + ':' + location.port);

    // Removes individual resource UI item
    socket.on('remove_ui_item', function(data) {
	jQuery('span#' + data['id']).parent().remove();
      });

    socket.on('new_item', function(data) {
	$('#item-container').append(data);
	$('#form-container').toggle(400);
	$('#form-container input[name="url"]').val('');
	$('#plus').css('opacity',1);
    });
    
    // UI refresh when data has changed
    socket.on('message', function(data){
	jQuery('#item-container').replaceWith(data);
    });

    // Start removal from server
    $('body').on('click', '.remove', function(){
	var id = $(this).attr('id');
	socket.emit('remove_item', { 'item_id': id });
    });

    // Toggle add new -form
    $("#plus").click(function() {
	$("#plus").css("opacity") == 1 ? $("#plus").css("opacity",0.5) : $("#plus").css("opacity",1);
	$("#form-container").slideToggle('slow');
	$("input[name='url']").focus();
    });

    // Form submit -handler
    $(document).on('submit','form#new', function(event) {

	var url = "new-resource";
	console.log("submit handler accessed..");
	$.ajax({
	    type: "POST",
	    url: url,
	    data: $(this).serialize(),
	    error: function(data) {
		console.log("Form submit error: " +  data);
	    }
	});
	event.preventDefault();
    });
});
