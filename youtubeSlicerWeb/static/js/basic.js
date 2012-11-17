function getVideoDetails() {
	$('#warningImage').hide();
	var videoUrl = $('#videoUrl').val();
	var getVideoUrl = globalGetVideoUrl + '?videoUrl=' + videoUrl;
	$('#sliceVideoButton').attr("disabled", true);
	$('#downloadVideo').hide();
	$('#downloadSlice').hide();

	$.ajax({
	    url: getVideoUrl,
	    dataType: 'json',
	    success: getDetailsReponse,
	    error: function( data ) {
		$('#loadingVideo').hide();
		$('#warningImage').show();
	    }
	  });

//	$.getJSON(getVideoUrl, getDetailsReponse);
}

function showPreview(videoThumb){
	var videoUrl = $('#videoUrl').val();
	var domain = videoUrl.replace('http://','').replace('https://','').split(/[/?#]/)[0];

	$('#youtubeIFrame').hide();
	$('#vimeoIFrame').hide();	
	$('#videoThumb').hide();

	if (domain == 'www.youtube.com')
	{
		var embedURL = 'http://www.youtube.com/embed/' + glovalCurrentVideoId
		$('#youtubeIFrame').show();
		$('#youtubeIFrame').attr("src",embedURL);
	}
	else if (domain == 'vimeo.com')
	{
		var embedURL = 'http://player.vimeo.com/video/' + glovalCurrentVideoId
		$('#vimeoIFrame').show();
		$('#vimeoIFrame').attr("src",embedURL);
	}
	else
	{
		$('#videoThumb').show();
		$('#vimeoIFrame').attr("src",videoThumb);
	}

}
	
function getDetailsReponse(responseObject)
{
	$('#videoThumb').attr("src",responseObject['thumbnail']);
	glovalCurrentVideoId = responseObject['videoId']
	
	showPreview(responseObject['thumbnail']);

	$('#loadingVideo').show();
	var getVideoUrl = globalGetVideo + '?videoUrl=' + responseObject['originalUrl'];

	$.ajax({
	    url: getVideoUrl,
	    dataType: 'json',
	    success: getVideoResponse,
	    error: function( data ) {
		$('#loadingVideo').hide();
		$('#warningImage').show();
	    }
	  });
	//$.getJSON(getVideoUrl, getVideoResponse);
	}

function getVideoResponse(responseObject)
{
	$('#loadingVideo').hide();
	$('#sliceVideoButton').attr("disabled", false);
	var downloadLink = globalDownloadVideo + '?videoId=' + glovalCurrentVideoId;
	
	$('#downloadVideo').show();
	$('#downloadVideo').attr("href",downloadLink);
	$('#downloadVideo').html('Download');
	
	//var newLink = $('<a href=' + downloadLink + '> Download </a>'); 
	//$('#videoParagraph').append(newLink);
	
	}


function sliceCurrentVid()
{
	
	var startMin = parseFloat($('#startMin').val());
	var startSecond = parseFloat($('#startSecond').val());
	var endMin = parseFloat($('#endMin').val());
	var endSecond = parseFloat($('#endSecond').val());
	startSecond = startMin*60 + startSecond;
	endSecond = endMin*60 + endSecond;
	var getVideoUrl = globalsliceVideo + '?videoId=' + glovalCurrentVideoId + '&startSecond=' + startSecond + '&endSecond=' + endSecond;
	$('#loadingSlice').show();
	$('#downloadSlice').hide();
	$('#sliceWarningImage').hide();
	$.ajax({
	    url: getVideoUrl,
	    dataType: 'json',
	    success: getSlicerResponse,
	    error: function( data ) {
		$('#loadingSlice').hide();
		$('#sliceWarningImage').show();
	    }
	  });
//	$.getJSON(getVideoUrl, getSlicerResponse);
	}


function getSlicerResponse(responseObject)
{
	$('#loadingSlice').hide();
	var videoId = responseObject['videoId'];
	var downloadLink = globalDownloadVideo + '?videoId=' + videoId;
	
	$('#downloadSlice').show();
	$('#downloadSlice').attr("href",downloadLink);
	$('#downloadSlice').html('Download');
	//var newLink = $('<a href=' + downloadLink + '> Download slice </a>'); 
	//$('#sliceParagraph').append(newLink);
}
