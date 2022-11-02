  # <button class="test btn btn-primary">Testing</button>
  # <table class="table table-striped">
  #     <thead>
  #         <tr>
  #             <th scope="col"></th>
  #             <th scope="col">AppName</th>
  #             <th scope="col">Last Online</th>
  #             <th scope="col">Last Offline</th>
  #         </tr>
  #     </thead>
  #     <tbody id="display">
  #     </tbody>
  # </table>
        # <script>
        #     $(document).ready(function(){
        #         $('.test').on('click', function(){
        #             $.ajax({
        #                 url:"{%url 'live-data'%}",
        #                 type:'GET',
        #                 success:function(res){
        #                     var _html=''
        #                     res.forEach((data, index)=>{
        #                         data=res[index]
        #                         const appname=data.appname
        #                         const url=data.url
        #                         const status=data.online
        #                         const date=data.date
        #                         const count='{{forloop.counter}}'
        #                         display.innerHTML+=`
        #                             <th scope="row">${count}</th>
        #                             <td>${appname}</td>
        #                             <td class="table-success">${date}</td>
        #                             <td class="table-danger">ccc</td>
        #                         `
        #                     });
        #                 }
        #             });
        #         });
        #     });
        # </script>





#       // LOAD MORE PAGE 
#       $(document).ready(function(){
#         $('#loadmoreBtn').on('click', function(){
#           var _currentResult=$(".page-content").length;
#           var country='{{country}}'
#           // RUN AJAX (ORIGINAL)
#           $.ajax({
#             url:"{%url 'load-page' location country%}",
#             type:'POST',
#             data:{
#               'country':country,
#               'offset':_currentResult,
#               'csrfmiddlewaretoken':"{{csrf_token}}"
#             },
#             dataType:'json',
#             beforeSend:function(){
#               $('#loadmoreBtn').attr('disabled',true);
#               $('.load-more-icon').addClass('fa-spin');
#             },
#             success:function(res){
#               var _html='';
#               var json_UserPics=$.parseJSON(res.pics_json);
#               var json_data=$.parseJSON(res.posts_json);
#               var postCommentCount=res.postCommentCount
#               var requestUser=res.requestUser
#               var verified=res.is_verified
#               json_data.forEach((data, index)=>{
#                 const commentCount=postCommentCount[index];
#                 const profilePICS=json_UserPics[index];
#                 const is_verified=verified[index]
#                 const content=data.fields.content
#                 const postTime=timeAgo(data.fields.date)
#                 const loadlikeCount=data.fields.liked.length
#                 const post_id=data.pk
#                 const postID=data.pk
#                 const postUsername=data.fields.username
#                 const room=data.fields.room
#                 const userID=data.fields.user
#                 const postlikes=data.fields.liked
#                 const requestUserName ="{{request.user}}"
#                 const country=data.fields.country
#                 _html+=`
#                 <div class="page-content">
#                   <div class="toast-header" style="background-color:#73c2fb;">
#                     <span><img src="${profilePICS}" alt="image" class="rounded mx-auto d-block" style="vertical-align:middle; width:50px; height:50px; border-radius:50%;"></span>
#                       ${requestUser != userID?`<a href="${room}/userprofile/${postUsername}" class="me-auto ps-2 text-secondary" style="text-decoration:none; overflow:auto;"><strong>${postUsername} ${is_verified 
#                       ?'<i class="bi bi-patch-check-fill text-white" style="font-size:medium;"></i>' 
#                       :''}</strong></a>`:`<a href="${room}/myprofile/${postUsername}" class="me-auto ps-2 text-secondary" style="text-decoration:none; overflow:auto;"><strong>${postUsername} ${is_verified 
#                       ?'<i class="bi bi-patch-check-fill text-white" style="font-size:medium;"></i>':''}</strong></a>`}
#                     <span class="ps-2">${userID==requestUser?'':`<a href="${room}/checkview/${requestUserName}/${postUsername}/" class="badge rounded-pill btn-outline-light" style="color:#fff; background-color:#233a4b;"><i class="fa fa-lg fa-envelope"></i></a>`}</span>
#                   </div>
#                   <div class="toast-body" style="border-left:3px solid white; border-right:1px solid white;">
#                     <div class="post" style="text-align:justify; text-justify:inter-word;">
#                       <div style="color:#73c2fb; font-size:small;"><small>${postTime}</small></div>
#                       <p class="postcontent" style="color:white;">${content}</p>
#                       <button onclick="readMore(this)" class="btn-sm btn-outline-light py-0" style="font-size:0.4em; display:inline-block;">Read More</button>
#                     </div>
#                   </div>
#                   <div class="d-flex justify-content-around pt-4">
#                     ${ commentCount==0?`<button type="button" class="btn btn-sm position-relative" style="background-color:#457497;">
#                         <i class="fa-solid fa-comments fa-lg text-white"></i>
#                         <span class="  position-absolute top-0 start-100 translate-middle badge rounded-pill" style="background-color:#457497;">${commentCount}</span>
#                       </button>`
#                     :`<a href="${room}/${postID}">
#                         <button type="button" class="btn btn-sm position-relative" style="background-color:#457497;">
#                           <i class="fa-solid fa-comments fa-lg text-white"></i>
#                           <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill" style="background-color:#457497;">${commentCount}</span>
#                         </button>
#                       </a> 
#                     `}
#                     <form action="{%url 'like-unlike-post'%}" method="POST" class="like-form" id="${post_id}">
#                       <input type="hidden" name="post_id" value="${post_id}">
#                       <div class="wrap" style="position:relative; display:inline-block;">
#                         <button type="submit" class="like-btn${post_id} btn btn-sm position-relative text-white" style="background-color:#457497;">
#                           ${! postlikes.includes(requestUser)?'<i class="fa-solid fa-heart fa-lg text-light"></i>':'<i class="redheart fa-solid fa-heart fa-lg" style="color:#ff0268;"></i>'}
#                         </button>
#                         <span class="like-count${post_id} position-absolute top-0 start-100 translate-middle badge" style="position:absolute; top:0; right:0;">${loadlikeCount}</span>
#                       </div>
#                     </form>
#                     <div class="position-relative">
#                       <button type="button" class="btn btn-sm  text-white" style="background-color:#457497;"> Reply</button>
#                       <a href="${room}/${postID}" class="stretched-link"></a>
#                     </div>
#                     <style>
#                       .dropbtn{
#                         background-color:#233a4b;
#                         color:white;
#                         border:none;
#                         cursor:pointer;
#                       }
#                       .dropbtn:hover,
#                       .dropbtn:focus{
#                         background-color:#457497;
#                       }
#                       .dropdown{
#                         position:relative;
#                         display:inline-block;
#                       }
#                       .dropdown-content{
#                         display:none;
#                         position:absolute;
#                         background-color:#f1f1f1;
#                         min-width:160px;
#                         overflow:auto;
#                         box-shadow:0px 8px 16px 0px rgba(0, 0, 0, 0.2);
#                         z-index:1;
#                       }
#                       .dropdown-content a{
#                         color:black;
#                         padding:12px 16px;
#                         text-decoration:none;
#                         display:block;
#                       }
#                       .dropdown a:hover{
#                         background-color:#ddd
#                       }
#                       .show{
#                         display:block;
#                       }
#                     </style>
#                     <div class="dropdown">
#                       <button onclick="myFunction(this)" class="dropbtn btn btn-sm fa fa-lg fa-ellipsis-v"></button>
#                       <div id="myDropdown1" class="dropdown-content" style="border-radius:10px;">
#                         ${ requestUser==userID?`<a href="#home"><i class="fa  fa-cog"></i> Settings</a>`:`<a href="#contact"><i class="fa  fa-flag" style="color:#ff0268;"></i> Report</a>`}
#                         ${ requestUser==userID?`<a href="delete-post/${room}/${country}/${postID}/"><i class="fa  fa-trash"></i> Delete</a>`:`<a href="#contact"><i class="fa  fa-ban" style="color:#ff0268;"></i> Block</a>` }
#                       </div>
#                     </div>
#                   </div>
#                 </div><hr  style="color:#73c2fb; height:3px;"><br>`
#               });
#               //LOAD MORE LIKE AND UNLIKE BUTTON
#               $(document).ready(function(){
#                 $('.like-form').submit(function(e){
#                   e.preventDefault()
#                   const post_id=$(this).attr('id')
#                   const likeText=$(".like-btn"+post_id).find("i").hasClass("redheart")?"Unlike":"Like"
#                   const trim=$.trim(likeText)
#                   const url=$(this).attr('action')
#                   let res;
#                   const likes=$(`.like-count${post_id}`).text()
#                   const trimCount=parseInt(likes)
#                   $.ajax({
#                     type:"POST",
#                     url:url,
#                     data:{
#                       'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
#                       'post_id':post_id,
#                     },
#                     success:function(response){
#                       if(trim === 'Unlike'){
#                         $(`.like-btn${post_id}`).html('<i class="fa-solid fa-heart fa-lg text-light"></i>')
#                         res=trimCount-1
#                       }else{
#                         $(`.like-btn${post_id}`).html('<i class="redheart fa-solid fa-heart fa-lg" style="color:#ff0268;"></i>')
#                         res=trimCount+1
#                       }
#                       $(`.like-count${post_id}`).text(res)
#                     },
#                     error:function(response){
#                       console.log('error', response)
#                     }
#                   });
#                 });
#               });
#               $(".post-wrapper").append(_html);
#               $("#loadmoreBtn").attr('disabled',false);
#               $(".load-more-icon").removeClass('fa-spin');
#               var _countTotal=$(".page-content").length;
#               if(_countTotal==res.totalResult){
#                 $("#loadmoreBtn").remove();
#               }
#               let noOfCharac=300;
#               let contents=document.querySelectorAll(".postcontent");
#               contents.forEach(postcontent=>{
#                 //If text length is less that noOfCharac... then hide the read more button
#                 if(postcontent.textContent.length<noOfCharac){
#                   postcontent.nextElementSibling.style.display ="none";
#                 }
#                 else{
#                   let displayText=postcontent.textContent.slice(0,noOfCharac);
#                   let moreText=postcontent.textContent.slice(noOfCharac);
#                   postcontent.innerHTML=`${displayText}<span class="dots">...</span><span class="hide more">${moreText}</span>`;
#                 }
#               });
#             }
#           });
#         });
#       });
      












#                     <div class="card ps-4 pe-4 pt-4">
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fab fa-tiktok" style="color: #000000;"></i> Tiktok is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fab fa-instagram" style="color: #e4405f;"></i> Instagram is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fab fa-facebook" style="color: #3b5998;"></i> Facebook is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fab fa-whatsapp" style="color: #075e54;"></i> Whatsapp is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fab fa-telegram" style="color: #0088cc;"></i> Telegram is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fa fa-snapchat" style="color: #fffc00;"></i> Snapchat is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fa fa-video-camera" style="color: #2d8cff;"></i> Zoom is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fab fa-facebook-messenger" style="color: #0084ff;"></i> Facebook Messenger is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fab fa-youtube" style="color: #c4302b;"></i> Youtube is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fa fa-youtube" style="color: #c4302b;"></i> Youtube is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fab fa-flickr" style="color: #0063dc;"></i> Flickr is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fab fa-twitter" style="color: #00acee;" style="color: #00acee;"></i> Twitter is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>



#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <span style="color: #e50914; font-family: serif;">N</span><i class="fab fa-netflix" style="color: #00acee;"></i> Netflix is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fab fa-google" style="color: #1a73e8;"></i><span style="color: #ea4335;">o</span><span style="color: #fbbc04;">o</span><span style="color: #4285f4;">g</span><span style="color: #34a853;">l</span><span style="color: red;">e</span> <span style="color: #1a73e8;">Maps</span> is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fab fa-google" style="color: #1a73e8;"></i><span style="color: #ea4335;">o</span><span style="color: #fbbc04;">o</span><span style="color: #4285f4;">g</span><span style="color: #34a853;">l</span><span style="color: red;">e</span> <span style="color: #1a73e8;">Meet</span> is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fab fa-"></i><span style="color: #003580;"> Booking</span><span style="color: #fff;">.com</span> is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fab fa-" style="color: #ff5a5f;"></i> <span style="color: #ffa200;">Audiomack</span> is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>



#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fa fa-dollar" style="color: #00d632;"></i> Cashapp is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fab fa-discord" style="color: #7289d9;"></i> Discord is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fab fa-linkedin-in" style="color: #0e76a8;"></i> LinkedIn is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fab fa-reddit" style="color: #ff4500;"></i> Reddit is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fa-brands fa-salesforce" style="color: #00acee;"></i> Saleforce is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fa fa-taxi" style="color: #000000;"></i> Taxify is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fab fa-uber" style="color: #000000;"></i> Uber is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fa fa-amazon" style="color: #000000;"></i> Amazon is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fa fa-paypal" style="color: #3b7bbf;"></i> PayPal is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fa fa-pinterest" style="color: #c8232c;"></i> Pinterest is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fa fa-apple" style="color: #555555;"></i> Apple is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fa fa-stack-exchange" style="color: #f47f24;"></i> Stack Overflow is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fa fa-tripadvisor" style="color: #00af87;"></i> Tripadvisor is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fa fa-tumblr" style="color: #34526f;"></i> Tumblr is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-danger" style="color: black;" role="alert">
#                             <i class="fa fa-twitch" style="color: #6441a5;"></i> Twitch is Down <span class="badge bg-danger" style=" color: #fff;">offline</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fab fa-wordpress" style="color: #21759b;"></i> Wordpress is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fa fa-wechat" style="color: #9de60b;"></i> Wechat is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fab fa-airbnb" style="color: #ff5a5f;"></i> Airbnb is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fab fa-spotify" style="color: #1db954;"></i> Spotify is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fa-brands fa-shopify" style="color: #96bf48;"></i> Shopify is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fa-brands fa-skype" style="color: #00aff0;"></i> Skype is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                         <div class="alert alert-success" style="color: black;" role="alert">
#                             <i class="fa-brands fa-meetup" style="color: #e51937;"></i> Meetup is Up and Running <span class="badge bg-success" style=" color: #fff;">Online</span>
#                         </div>
#                     </div>



























# def insights(request,pk):
#     tx=get_object_or_404(RegisteredUser,id=pk)
#     txid=tx.txID
#     inurl=RegisteredUser.objects.filter(txID=txid).values_list('inputURL',flat=True)
#     outurl=RegisteredUser.objects.filter(txID=txid).values_list('outputURL',flat=True)
#     for _ in inurl:
#         inputurl=_
#     for _ in outurl:
#         outputurl=_
#     vis=Visitor.objects.filter(txID=txid)
#     tot=vis.count()
#     if tot==0:
#         tot=1
#     loclick=vis.values('location').annotate(clicks=Count('ip'),perc=Count('location')*100/tot)
#     u_=vis.values('ip','location').annotate(clicks=Count('ip'))
#     lc=[x['location'] for x in u_]
#     a=dict(Counter(lc))
#     loc=[]
#     for j in set(lc):
#         if j in a:
#             c='location'
#             u_v='visitor'
#             egb={c:j,u_v:a[j]}
#             loc.append(egb)    
#     # THIS MERGE 2 QUERYSET TOGETHER (LOCLICK AND LOC) TOGETHER WHERE 'LOCATION ARE THE SAME
#     d=defaultdict(dict)
#     for loc in (loclick,loc):
#         for elem in loc:
#             d[elem['location']].update(elem)
#     n_loc=d.values()
#     # ************************DEVICE PERCENTAGE********************************
#     dee=vis.values('location','type_of_device').annotate(count=Count('type_of_device'))
#     tot=dee.aggregate(Sum('count'))
#     device=dee.values('type_of_device').annotate(count=Count('type_of_device'))
#     des=device.filter(type_of_device='Desktop').values_list('count',flat=True)
#     ta=device.filter(type_of_device='Tablet').values_list('count',flat=True)
#     mo=device.filter(type_of_device='Mobile').values_list('count',flat=True)
#     total=tot['count__sum']
#     if des:
#         for i in des:
#             desk=str(round(i*100/total))+'%'
#     else:
#         desk=str(0)+'%'
#     if ta:
#         for i in ta:
#             tab=str(round(i*100/total))+'%'
#     else:
#         tab=str(0)+'%'
#     if mo:
#         for i in mo:
#             mob=str(round(i*100/total))+'%'
#     else:
#         mob=str(0)+'%'
#     context={
#         'inputurl':inputurl,'outputurl':outputurl,
#         'loc':a,'data':n_loc,'total':tot,
#         'desktop':desk,'tablet':tab,'mobile':mob,
#         'total':total,'id':pk,
#     }
#     return render(request,'insights.html',context)