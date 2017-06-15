<?php
// Routes

$app->get('/', function ($request, $response, $args) {
    return $this->renderer->render($response, 'index.phtml', $args);
});

$app->get('/{name}', function ($request, $response, $args) {
	
    return $this->renderer->render($response, 'info.phtml', $args);
});	
