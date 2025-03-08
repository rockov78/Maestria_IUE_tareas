use anyhow::Result;
use futures::future::join_all;
use reqwest::Client;
use serde_json::from_str;

pub async fn download_temperatures() -> Result<Vec<(String, String)>> {
    let cities = vec![
        "paris",
        "london",
        "tokyo",
        "new york",
        "sydney",
        "moscow",
        "cairo",
        "beijing",
        "mumbai",
        "rio de janeiro",
    ];

    let client = Client::new();

    let futures_vec = cities.iter().map(|city| {
        let client = client.clone();
        let city = city.to_string();
        async move {
            let city_encoded = city.replace(" ", "%20");
            let url = format!("https://weather.siel.com.co/city/{}/temp/max", city_encoded);

            // Enviar la solicitud HTTP
            let response = client
                .get(&url)
                .header("Authorization", "Bearer secret-token-1234")
                .send()
                .await;

            // Procesar la respuesta
            let resp_text = match response {
                Ok(resp) => match resp.text().await {
                    Ok(text) => text,
                    Err(e) => {
                        eprintln!("Error al leer el texto para {}: {}", city, e);
                        "".to_string()
                    }
                },
                Err(e) => {
                    eprintln!("Error al descargar datos para {}: {}", city, e);
                    "".to_string()
                }
            };

            // Intentar parsear la respuesta como JSON
            let temps_first_ten = if resp_text.trim().starts_with('[') {
                // Se espera un arreglo JSON
                match from_str::<Vec<f64>>(&resp_text) {
                    Ok(nums) => nums
                        .into_iter()
                        .take(10)
                        .map(|n| n.to_string())
                        .collect::<Vec<String>>()
                        .join(","),
                    Err(e) => {
                        eprintln!("Error al parsear JSON para {}: {}", city, e);
                        "".to_string()
                    }
                }
            } else {
                // Si no es JSON, se procesa como CSV simple
                let temps: Vec<&str> = resp_text
                    .split(',')
                    .map(|s| s.trim())
                    .filter(|s| !s.is_empty())
                    .collect();
                temps.into_iter().take(10).collect::<Vec<&str>>().join(",")
            };

            (city, temps_first_ten)
        }
    });

    let results = join_all(futures_vec).await;
    Ok(results)
}
