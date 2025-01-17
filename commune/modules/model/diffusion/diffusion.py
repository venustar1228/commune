import commune as c
from diffusers import DiffusionPipeline
import torch
class DiffisionPipeline(c.Module):
    def __init__(self, config=None, **kwargs):
        config =  self.set_config(config=config, kwargs=kwargs)
        self.set_model(config.model)

    def set_model(self, model:str):
        c.ensure_lib("diffusers")
        from diffusers import DiffusionPipeline
        import torch

        # load both base & refiner
        self.base = DiffusionPipeline.from_pretrained(model, torch_dtype=torch.float16, variant=self.config.variant, use_safetensors=True
        )
        self.base.to(self.config.device)

    def generate(self, 
                prompt: str = "A majestic lion jumping from a big stone at night",
                n_steps: int =40,
                high_noise_frac: float = 0.8,
                output_type: str ="image"):
            """
            Generate an image from a prompt using the diffusion model.
            """


            # run both experts
            images = self.base(
                prompt=prompt,
                num_inference_steps=n_steps,
                denoising_end=high_noise_frac,
                output_type=output_type,
            ).images


            return images


    @classmethod
    def test(cls, **kwargs):
        self = cls(**kwargs)
        return self.generate()