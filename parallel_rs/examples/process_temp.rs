use tokio;
use concurrence_rs::download_temperatures;
use parallel_rs::process_temperatures;

#[tokio::main]
async fn main() {
    // Se descargan los datos de forma concurrente.
    match download_temperatures().await {
        Ok(data) => {
            // Se procesan los datos en paralelo.
            let results = process_temperatures(data);
            // Se muestran los resultados.
            for (city, avg, std_dev) in results {
                println!("Ciudad: {}\n  Promedio: {}\n  Desviación Estándar: {}\n", city, avg, std_dev);
            }
        }
        Err(e) => {
            eprintln!("Error al descargar temperaturas: {:?}", e);
        }
    }
}
