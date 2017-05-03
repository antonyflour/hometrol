/**
 * Created by anton on 03/05/2017.
 */
$('#menuButton').click(function()
{
    $('.menu').
    animate({"left":"0px"}, 500);
});

$('.closeButton').click(function()
{
    $('.menu').animate({"left":"-200px"}, 500);
});