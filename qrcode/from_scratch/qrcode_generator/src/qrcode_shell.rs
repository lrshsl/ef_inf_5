
pub fn generate_qrcode(input: &str) {
    // let meta_data = QrMetaData::from(data);
    // let qr_generator = QrCodeGenerator::from_meta_data(meta_data);
    
    // let data_bits = qr_generator.generate();
    
    // Prepare a grid that can draw_the bits
    // let grid = Grid::new(
        // meta_data.size,
        // data_bits);
    
    let data_bits: Vec<Bit> = vec![
        0,1,1,1,0,
        0,1,1,1,0,
        0,1,1,1,0,
    ];
    let grid = Grid::new((3, 5), data_bits)

    // Make window and draw the QrCode
    grid.draw();
}
