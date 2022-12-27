window.addEventListener('load',function(){
	//get elements
	var left = document.querySelector('.left');
	var right = document.querySelector('.right');
	var main = document.querySelector('.main');
	var mainWidth = main.offsetWidth;
	//the mouse slide left or right button
	main.addEventListener('mouseenter',function(){
		left.style.display = 'block';
		right.style.display = 'block';
		clearInterval(timer);
		timer = null; // clean the variable of counter
	})
	//mouse leave and button are hided
	main.addEventListener('mouseleave',function(){
		left.style.display = 'none';
		right.style.display = 'none';
		timer = setInterval(function() {
			//click and all the function
			right.click();
		}, 2000);
	})
	//create little circle
	var ul = main.querySelector('ul')
	var ol = main.querySelector('.circle')
	for (var i = 0; i < ul.children.length; i++) {
		//build a <li>
		var li = document.createElement('li');
		// record the number of little circle
		li.setAttribute('index', i);
		//insert <ol>
		ol.appendChild(li);
		li.addEventListener('click', function() {
			//clean <li> class name
			for (var i = 0; i < ol.children.length; i++) {
				ol.children[i].className = '';
			}
			//the current <li> set class
			this.className = 'current';
			var index = this.getAttribute('index');
			 // when click one little circle, give num
			num = index;
			// when click one little circle, give circle
			circle = index;
			// 5. click and move <ul>
			animate(ul, -index * mainWidth);
		})
	}
	ol.children[0].className = 'current';
	var first = ul.children[0].cloneNode(true);
	ul.appendChild(first);
	var num = 0;
	var circle = 0;
	var flag = true;
	// right button
	right.addEventListener('click',function(){
	if(flag){
			flag = false;
			if(num == ul.children.length-1){
				ul.style.left = 0;
				num = 0;
			}
			num++;
			animate(ul, -num*mainWidth,function(){
				flag = true;
			});
			circle++;
			if (circle == ol.children.length) {
				circle = 0;
			}
			circleChange();
		}
	});
	// left button
	left.addEventListener('click',function(){
	if(flag){
			flag = false;
			if(num == 0){
				num = ul.children.length - 1;
				ul.style.left = -num * mainWidth + 'px';
			}
			num--;
			animate(ul, -num*mainWidth, function(){
				flag = true;
			});
			circle--;
			if (circle < 0) {
				circle = ol.children.length - 1;
			}
			circleChange();
		}
	});
	function circleChange() {
		for (var i = 0; i < ol.children.length; i++) {
			ol.children[i].className = '';
		}
		ol.children[circle].className = 'current';
	}
	// auto play
	var timer = setInterval(function() {
		right.click();
	}, 2000);
})
