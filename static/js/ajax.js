$(document).ready(function(){

	$("#submit").click(function(){
	
		var word = $("input[name='message']").val();
		var list = $("input[name='list']").val();
		//alert(word);
		var data = {"param" : word, "list" : list};
		$.ajax({
			
			type: "POST",
			url: "/filter",
			data: data,
			dataType: "json",
			success: function(data){
				$("#filterList").html("Word list is <label>" + data.list + "</label>");
				$("#result").html("After filtering, result is <label>" + data.result + "</label>");
			
			}
		
		
		});
		return false;
	});

});