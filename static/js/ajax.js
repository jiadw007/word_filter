$(document).ready(function(){

	$("#submit").click(function(){
	
		var word = $("input[name='message']").val();
		//alert(word);
		var data = {"param" : word};
		$.ajax({
			
			type: "POST",
			url: "/filter",
			data: data,
			dataType: "text",
			success: function(data){
			
				$("#result").html(data);
			
			
			}
		
		
		
		
		});
	});

});