function fontAuto(width){//width表示效果图的宽度
	var screenWidth=document.documentElement.clientWidth;//屏幕的宽度
	//document.documentElement表示html标签
	if(screenWidth>=width)//当设备的宽度大于等于效果图的宽度
	{
		document.documentElement.style.fontSize="625%";
	}
	else{//当设备的宽度小于效果图的宽度
		document.documentElement.style.fontSize=(625*screenWidth/width)+"%";
	}
	
}

fontAuto(750);//网页加载的时候触发

window.onresize=function(){//当网页宽度发生变化时触发函数
	fontAuto(750);
}