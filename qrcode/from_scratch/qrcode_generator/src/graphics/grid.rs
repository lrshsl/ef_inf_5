use crate::{
    Bit,
};
use macroquad::prelude::*;


pub fn draw_grid(size: [u32; 2], data: &Vec<u8>) {
    let screen_size = screen_width().min(screen_height());
    let grid = Grid::new(size, screen_size);
    for col in 0..size[0] {
        for row in 0..size[1] {
            let color = data[0];
            grid.draw_square_at(col, row, color);
        }
    }
}

pub struct Grid {
    screen_size: f32,
    margin: [f32; 2],
    size: [u8; 2],
}

impl Grid {
    pub fn new(size: [u8, 2], screen_size: [f32; 2]) -> Self {
        let screen_
        let margin_x = 
        Self {
            screen_size,
            margin,
            size,
        }
    }
    fn draw_square_at(&self, col: u8, row: u8, color: u8) {
        let x = self.margin + col * self.cell_size;
    }
}
