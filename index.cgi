#!C:\xampp\perl\bin\perl.exe

use strict;
use CGI;

my $cgi = new CGI;

print $cgi->header('text/html');

print $cgi->start_html(
-head => (
			$cgi->Link({}),
			-title => 'Site noticia',
			-encoding => 'UTF-8',
			-style => [{'src' => './style/estilo.css'}]
		)
);

print $cgi->body({'class' => 'home'}, 

	$cgi->div({'id' => 'container'},
		$cgi->div({'id' => 'topo'},
			$cgi->h1({'class' => 'logo'}, 'Notícias Cidade'),
			$cgi->ul({'id' => 'navegacao'}, 
				$cgi->li({'class' => 'primeiro'},$cgi->a({'id' => "home",-href=>"index.cgi"},"Home")),
				$cgi->li($cgi->a({'id' => "brasil",-href=>"index.cgi"},"Brasil")),
				$cgi->li($cgi->a({'id' => "internacional",-href=>"index.cgi"},"Internacional")),
				$cgi->li($cgi->a({'id' => "economia",-href=>"index.cgi"},"Economia")),
				$cgi->li($cgi->a({'id' => "saude",-href=>"index.cgi"},"Saude")),
				$cgi->li($cgi->a({'id' => "ciencia",-href=>"index.cgi"},"Ciencia")),
				$cgi->li($cgi->a({'id' => "fotos",-href=>"index.cgi"},"Fotos"))
			)
		),
		
		$cgi->div({'class' => 'conteudo'},
	
			$cgi->div({'id' => 'primario'},
				$cgi->div({'class' => 'caixa destaque'}, 
					$cgi->h2('Destaque'),
					$cgi->div({'class' => 'caixa-conteudo'},
						$cgi->h3('Nova legislacao'),
						$cgi->img({'class' => 'imagem-principal', 'src' => 'imagens/taxi.jpg', 'width' => '100%'}),
						$cgi->p('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer id pretium orci. Vestibulum quis maximus sapien, vel porta quam.'),
						$cgi->a({-href=>""},"Leia mais")
					)
				),
				
				$cgi->div({'class' => 'caixa'}, 
					$cgi->h2('Mundo'),
					$cgi->div({'class' => 'caixa-conteudo'},
						$cgi->ul({'id' => 'lista-noticias'},
							$cgi->li($cgi->a({-href => ""},
								$cgi->img({'src' => 'imagens/tecnologia.jpg', 'width' => '80'}),
								$cgi->h3('Novas tecnologias'),
								$cgi->p('Lorem ipsum dolor sit amet, consectetur ...'),
							)),
							$cgi->li($cgi->a({-href => ""},
								$cgi->img({'src' => 'imagens/tecnologia.jpg', 'width' => '80'}),
								$cgi->h3('Novas tecnologias'),
								$cgi->p('Lorem ipsum dolor sit amet, consectetur ...'),
							)),
							$cgi->li($cgi->a({-href => ""},
								$cgi->img({'src' => 'imagens/tecnologia.jpg', 'width' => '80'}),
								$cgi->h3('Novas tecnologias'),
								$cgi->p('Lorem ipsum dolor sit amet, consectetur ...'),
							)),
							$cgi->li($cgi->a({-href => ""},
								$cgi->img({'src' => 'imagens/tecnologia.jpg', 'width' => '80'}),
								$cgi->h3('Novas tecnologias'),
								$cgi->p('Lorem ipsum dolor sit amet, consectetur ...'),
							))
						)
					)
				)
			),
			
			$cgi->div({'id' => 'secundario'},
				$cgi->div({'class' => 'caixa entrevista'},
					$cgi->h2('Ultima entrevista'),
					$cgi->div({'class' => 'caixa-conteudo'},
						$cgi->h2('Entrevista com Felipe Silva'),
						$cgi->img({'class' => 'imagem-principal','src' => 'imagens/doutor.jpg', 'width' => '100%'}),
						$cgi->p('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer id pretium orci. Vestibulum quis maximus sapien, vel porta quam.'),
						$cgi->a({-href=>""},"Leia mais")
					)
				)
			)
		)
	)
	
	

);



print $cgi->end_html();