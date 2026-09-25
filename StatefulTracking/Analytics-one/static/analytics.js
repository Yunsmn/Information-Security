var uid = null;
var cookies = document.cookie.split('; ');

for (var i = 0; i < cookies.length; i++) {
    if (cookies[i].startsWith('analytics_id=')) {
        uid = cookies[i].split('=')[1];
    }
}

if (uid === null) {
    uid = Math.random().toString(16).slice(2);
    document.cookie = 'analytics_id=' + uid + '; max-age=31536000; path=/';
}

new Image().src = 'http://analytics.lab:9100/?uid=' + uid + '&page=' + location.href;
