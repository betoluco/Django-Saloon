function readCookie(ckname){
	var name = ckname+"=";
	if(document.cookie){
		var ckarray = document.cookie.split(';');
		for(var i=0; i<ckarray.length; i++){
			var ck = ckarray[i];
			while(ck.charAt(0) == 0) ck = ck.substring(1,ck.length);
			if(ck.indexOf(name) == 0) return ck.substring(name.length, ck.length)
		}
		return null;
	}
	return null;
}