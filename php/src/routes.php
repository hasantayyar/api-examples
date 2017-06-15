<?php
// Routes

$endPoint = "https://sandbox.bitwala.io";

function get($path){

}
function post($path, $options){
  
} 

$app->get('/', function ($request, $response, $args) {
    return $this->renderer->render($response, 'index.phtml', $args);
});

$app->get('/info', function ($request, $response, $args) {
    return $this->renderer->render($response, 'info.phtml', $args);
});

$app->get('/inputs', function ($request, $response, $args) {
    $data = get($endPoint.'/');
    return $response->withJson($data);
});

$app->get('/outputs', function ($request, $response, $args) {

    return $response->withJson($data);
});
