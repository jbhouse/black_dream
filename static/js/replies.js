$('div.replies-list').on('click','a',function(e){
  e.preventDefault();
  var that = $(this)
  var replyId = that.attr('id').slice(6,that.attr('id').length)
  deleteReply();
  function deleteReply(){
    $.ajax({
      url : "/replies/delete/"+replyId,
      type : "DELETE",
      data : {replyId:replyId, replyto:replyObject},
      success : function(json){
        $('#reply-'+json.id).parent().parent().addClass('hidden')
      }
    })
  }
})
//
// $('#reply-button').on('click', function(e){
//   e.preventDefault();
//   var that = $(this)
//   console.log(that);
// })

$('.reply-form').on('submit',function(e){
  e.preventDefault();
  var that = $(this)
  var reply = $('#reply').val()
  var replyId = document.getElementById('reply-button').getAttribute('name').slice(12,document.getElementById('reply-button').getAttribute('name').length)
  makeReply();
  function makeReply(){
    $.ajax({
      url       : "/replies/create/",
      type      : "POST",
      data      : {reply:reply, replyId:replyId, replyto:replyObject},
      success : function(json){
        $('div.replies-list').prepend("<div><h4>"+json.text+"</h4><p><a class='delete' id='reply-"+json.id+"' href='#'><span class='glyphicon glyphicon-remove text-danger'></span><span class='text-danger icon-label'>Delete</span></a></p></div>")
        document.getElementById('reply').value = ''
      }
    })
  }
})
