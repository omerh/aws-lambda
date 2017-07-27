exports.handler = (event, context, callback) => {
    var http = require('https');
    var querystring = require('querystring')
    var oncall = '';
    
    console.log('setting options');
    var options = {
    	host: 'api.pagerduty.com',
    	path: '/oncalls',
    	headers: {
    		"Accept": "application/vnd.pagerduty+json;version=2",
      		"Authorization": "Token token=[Your ENV VAR Token]"
    	}
    };
    
    console.log('sending request pagerduty api');
    var request = http.get(options, function(response){
        var body = "";
        console.log('reading response');
        response.on('data', function(chunk) {
        console.log('BODY: ' + chunk)
        body += chunk
      });
     
      response.on('end', function(){
          console.log('response ended');
         var result = JSON.parse(body);
         oncall = 'Oncall is ' + result.oncalls[0]['user']['summary'];
         callback(null, oncall);
      })
    });
};

