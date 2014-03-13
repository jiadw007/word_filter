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
				$("#filterList").html(data.list);
				$("#result").html(data.result);
			
			
			}
		
		
		
		
		});
	});

});