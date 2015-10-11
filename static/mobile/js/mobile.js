// JavaScript Document
window.onload = function(){
	
	//出现美女列表
	var obtn = document.getElementById('btn_list');
	var ogirl = document.getElementById('allgirl');
	var obtn_n = document.getElementById('btn_no');
	var obtn_y = document.getElementById('btn_yes');
	var ali = ogirl.getElementsByTagName('ul')[0].getElementsByTagName('li');
	
	
	obtn.onclick=function(){
		ogirl.style.display='block';
	}
	
	obtn_n.onclick=function(){
		ogirl.style.display='none';
	}
	
	for(var i = 0, l = ali.length; i < l; i++){
		
		ali[i].onclick=function(){
			for(var j = 0; j < l; j++){
				ali[j].className='';
			}
			this.className='on';
			//alert(this.getElementsByTagName('span')[0].innerText);
			obtn_y.href = this.getElementsByTagName('span')[0].innerText;
		}
	}
}
