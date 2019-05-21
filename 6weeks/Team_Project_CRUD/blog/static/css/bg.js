
        function test(){
            var myTest = new Array(
                'https://images.unsplash.com/photo-1558251338-5098973ffeea?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80',
                'https://images.unsplash.com/photo-1556909172-bd5315ff61a0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80',
                'https://images.unsplash.com/photo-1558098403-3a5cbd106dd1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=3252&q=80',
                'https://images.unsplash.com/photo-1558197385-575ecbf37bef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80',
                'https://images.unsplash.com/photo-1558172443-381a52803532?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80',
                'https://images.unsplash.com/photo-1558200473-84096f5ac589?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80',
                'https://images.unsplash.com/photo-1554381316-e7ae6a16bdf4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2251&q=80',
                'https://images.unsplash.com/photo-1554406974-78933cec323f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2255&q=80',
                'https://images.unsplash.com/photo-1557812442-4c24fdfd3698?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2255&q=80',
                );


function randomItem(a) {
  return a[Math.floor(Math.random() * a.length)];
}

            var div = document.getElementById("imgbody");
           div.style.backgroundImage="linear-gradient(rgba(0,0,0,0.1), rgba(0, 0, 0, 0.6)),url("+randomItem(myTest)+")";
        }
