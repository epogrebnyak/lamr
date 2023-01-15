const path = require( "path" );
const fs = require('fs');

function parseSidebar () {
    fp = path.resolve(__dirname, 'sidebar.json')
    data = fs.readFileSync(fp, 'utf8');
    return JSON.parse(data) || {} 
}


