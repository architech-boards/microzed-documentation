function select_text( containerid ) {

    var node = document.getElementById( containerid );

    if ( document.selection ) {
        var range = document.body.createTextRange();
        range.moveToElementText( node  );
        range.select();
    } else if ( window.getSelection ) {
        var range = document.createRange();
        range.selectNode( node );
        window.getSelection().removeAllRanges();
        window.getSelection().addRange( range );
    }
}
