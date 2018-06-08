function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();    //fileReader 是Html5定义的
        reader.onload = function (e) {
            $('#portraitImg').attr('src', e.target.result);

        }
        reader.readAsDataURL(input.files[0]); //1读取结果  2reader.onload 设置了触发事件 即function(e) e是context
                                                //3.在触发的函数中设置 属性
    }
}

$("#portrait").change(function(){
    readURL(this);
});

// function setImgSize() {
//     var $imgW = $('#portraitimg').width();
//     var $imgH = $('#portraitimg').height();
//     if ($imgH > $imgW){
//
//     }
// }