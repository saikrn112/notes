import numpy as np

def calculate_psnr(original_image, reconstructed_image):
    # Assuming original_image and reconstructed_image are NumPy arrays
    mse = np.mean((original_image - reconstructed_image) ** 2)
    max_pixel_value = 255  # Assuming an 8-bit image
    psnr = 10 * np.log10((max_pixel_value ** 2) / mse)
    return psnr

def calculate_ssim(original_image, reconstructed_image):
    # Assuming original_image and reconstructed_image are NumPy arrays
    K1 = 0.01
    K2 = 0.03
    L = 255  # Assuming an 8-bit image

    C1 = (K1 * L) ** 2
    C2 = (K2 * L) ** 2

    original_mu = np.mean(original_image)
    reconstructed_mu = np.mean(reconstructed_image)

    original_sigma_sq = np.var(original_image)
    reconstructed_sigma_sq = np.var(reconstructed_image)
    covariance = np.cov(original_image.flatten(), reconstructed_image.flatten())[0, 1]

    numerator = (2 * original_mu * reconstructed_mu + C1) * (2 * covariance + C2)
    denominator = (original_mu ** 2 + reconstructed_mu ** 2 + C1) * (original_sigma_sq + reconstructed_sigma_sq + C2)

    ssim = numerator / denominator
    return ssim

# Example usage:
original_image = np.random.rand(256, 256, 3) * 255  # Replace this with your original image
reconstructed_image = original_image + np.random.normal(scale=10, size=original_image.shape)  # Example noise

# PSNR calculation
psnr_result = calculate_psnr(original_image, reconstructed_image)
print(f"PSNR: {psnr_result} dB")

# SSIM calculation
ssim_result = calculate_ssim(original_image, reconstructed_image)
print(f"SSIM: {ssim_result}")

