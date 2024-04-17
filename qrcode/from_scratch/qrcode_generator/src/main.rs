use macroquad::{self, window::next_frame};
use graphics::grid::draw_grid;
use utils::*;

mod graphics;
// mod qrcode_shell;
mod utils;
mod constants;

#[macroquad::main("QrCodeGenerator V0.1")]
async fn main() {
    let data_bits: Vec<u8> = vec![
        0,1,1,1,0,
        0,1,1,1,0,
        0,1,1,1,0,
    ];
    loop {
        draw_grid([3, 5], &data_bits);
        next_frame().await
    }
}
