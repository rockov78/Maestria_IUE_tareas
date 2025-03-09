use std::collections::HashMap;

/// Calcula el promedio simple de números contenidos en una cadena separada por comas.
/// Si no se pueden parsear números o la cadena está vacía, retorna 0.0.
pub fn promedio_simple(data: &str) -> f64 {
    let nums: Vec<f64> = data
        .split(',')
        .filter_map(|s| s.trim().parse::<f64>().ok())
        .collect();
    if nums.is_empty() {
        0.0
    } else {
        let sum: f64 = nums.iter().sum();
        sum / (nums.len() as f64)
    }
}

/// Calcula la desviación estándar poblacional a partir de una cadena de números separados por comas.
pub fn desviacion_estandar(data: &str) -> f64 {
    let nums: Vec<f64> = data
        .split(',')
        .filter_map(|s| s.trim().parse::<f64>().ok())
        .collect();
    let n = nums.len();
    if n == 0 {
        return 0.0;
    }
    let avg = promedio_simple(data);
    let variance = nums.iter().map(|x| (x - avg).powi(2)).sum::<f64>() / (n as f64);
    variance.sqrt()
}

/// Calcula el promedio móvil de los números en la cadena usando una ventana de tamaño `window`.
/// Retorna un vector con cada promedio; si window es 0 o mayor que el número de datos, retorna un vector vacío.
pub fn promedio_movil(data: &str, window: usize) -> Vec<f64> {
    let nums: Vec<f64> = data
        .split(',')
        .filter_map(|s| s.trim().parse::<f64>().ok())
        .collect();
    if window == 0 || window > nums.len() {
        return vec![];
    }
    let mut mov_averages = Vec::new();
    for i in 0..=(nums.len() - window) {
        let slice = &nums[i..i + window];
        let sum: f64 = slice.iter().sum();
        mov_averages.push(sum / (window as f64));
    }
    mov_averages
}

/// Calcula la(s) moda(s) de una lista de números.
/// Se utiliza la representación en bits para sortear la falta de Eq/Hash en f64.
/// Retorna un vector con los números que aparecen con mayor frecuencia, ordenados.
pub fn calcular_moda(lista: &[f64]) -> Vec<f64> {
    let mut freq: HashMap<u64, usize> = HashMap::new();
    for &num in lista {
        // Usamos los bits del f64 como clave
        let bits = num.to_bits();
        *freq.entry(bits).or_insert(0) += 1;
    }
    if freq.is_empty() {
        return vec![];
    }
    let max_freq = freq.values().cloned().max().unwrap();
    let mut modes: Vec<f64> = freq
        .into_iter()
        .filter_map(|(bits, count)| {
            if count == max_freq {
                Some(f64::from_bits(bits))
            } else {
                None
            }
        })
        .collect();
    // Ordenamos los modos
    modes.sort_by(|a, b| a.partial_cmp(b).unwrap());
    modes
}

