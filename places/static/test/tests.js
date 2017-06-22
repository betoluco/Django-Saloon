QUnit.test( "Sanity check", function( assert ) {
  assert.ok( 1 == "1", "Passed!" );
});

QUnit.test("readCookie retrieves the cookie content", function(assert){
	document.cookie = "test=Test cookie";
	assert.equal(readCookie("test"), "Test cookie");
});