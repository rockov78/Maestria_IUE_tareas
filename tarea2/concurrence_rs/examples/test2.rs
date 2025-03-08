use concurrence_rs::download_temperatures;

#[tokio::main]
async fn main() {
    // Llamamos a la función asíncrona para descargar las temperaturas.
    match download_temperatures().await {
        Ok(results) => {
            // Iteramos sobre cada resultado y lo imprimimos.
            for (city, temps) in results {
                println!("Ciudad: {}\nTemperaturas: {}\n", city, temps);
            }
        }
        Err(e) => eprintln!("Error al descargar temperaturas: {:?}", e),
    }
}
