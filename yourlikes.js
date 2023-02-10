$( document ).ready(function() {
    var scaleCurve = mojs.easing.path('M0,100 L25,99.9999983 C26.2328835,75.0708847 19.7847843,0 100,0');
       var el = document.querySelector('.button'),
       
        timeline = new mojs.Timeline(),

        shape1 = new mojs.Burst({
            parent: el,
            radius:   { 0: 100 },
            angle:    { 0: 45 },
            y: -10,
            count:    10,
            radius:       100,
        details: {
                shape:        'circle',
                radius:       30,
                fill:         [ 'red', 'white' ],
                strokeWidth:  15,
                duration:     500,
            }
        });
    
    
        shape2 = new mojs.Shape({
            duration : 900,
            onUpdate: function(progress) {
                var scaleProgress = scaleCurve(progress);
                el.style.WebkitTransform = el.style.transform = 'scale3d(' + scaleProgress + ',' + scaleProgress + ',1)';
            }
        });
        shape3 = new mojs.Burst({
            parent: el,
            radius:   { 0: 100 },
            angle:    { 0: -45 },
            y: -10,
            count:    10,
            radius:       125,
        details: {
            shape:        'circle',
            radius:       30,
            fill:         [ 'white', 'red' ],
            strokeWidth:  15,
            duration:     400,
        }
        });
    
    timeline.add(shape1, shape2, shape3);
    
    

    $( ".button" ).click(function() {
        if ($(this).hasClass('active')){
            $(this).removeClass('active');
        }else{
      timeline.play();
      $(this).addClass('active');
        }
    });
    
    
    });