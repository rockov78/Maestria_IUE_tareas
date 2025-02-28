use anyhow::Result;
use futures::future::join_all;
use reqwest::Client;

/// Función asíncrona que descarga los datos de una ciudad.
/// Envía el header de autorización y toma solo las primeras 10 temperaturas.
async fn download_for_city(client: &Client, city: &str) -> Result<(String, String)> {
    // Se reemplazan los espacios por %20 para formar una URL válida
    let city_encoded = city.replace(" ", "%20");
    let url = format!("https://weather.siel.com.co/city/{}/temp/max", city_encoded);
    
    let resp = client
        .get(&url)
        .header("Authorization", "Bearer secret-token-1234")
        .send()
        .await?
        .text()
        .await?;
    
    // Se asume que la respuesta es una lista separada por comas
    let temps: Vec<&str> = resp
        .split(',')
        .map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .collect();
    let first_ten: Vec<&str> = temps.into_iter().take(10).collect();
    let temps_first_ten = first_ten.join(",");
    
    Ok((city.to_string(), temps_first_ten))
}

#[tokio::main]
async fn main() -> Result<()> {
    // Lista de ciudades a consultar
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

    // Crear un future para cada consulta y ejecutarlos en forma concurrente
    let futures_vec = cities.iter().map(|city| download_for_city(&client, city));
    let results = join_all(futures_vec).await;

    // Imprimir el resultado de cada consulta
    for res in results {
        match res {
            Ok((city, temps)) => println!("City: {} -> Temps: {}", city, temps),
            Err(e) => eprintln!("Error: {:?}", e),
        }
    }

    Ok(())
}
