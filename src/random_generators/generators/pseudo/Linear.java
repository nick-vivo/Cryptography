package random_generators.generators.pseudo;

import random_generators.generators.Generator;

public class Linear implements Generator 
{

    final int coef, increment, modulus;
    int seed;

    final static int basic_seed = 2, basic_coef = 45, basic_increment = 21, basic_modulus = 101; 

    public Linear(final int seed, final int coef, final int increment, final int modulus)
    {
        this.seed = seed;
        this.coef = coef;
        this.increment = increment;
        this.modulus = modulus;
    }

    public Linear(final int seed)
    {
        this(seed, basic_coef, basic_increment, basic_modulus);
    }

    public Linear()
    {
        this(basic_seed, basic_coef, basic_increment, basic_modulus);
    }

    @Override
    public int generate()
    {
        this.seed = (this.coef * this.seed + this.increment) % this.modulus;
        return this.seed;
    }

    @Override
    public int generate(final int max)
    {
        this.seed = (this.coef * this.seed + this.increment) % max;
        return this.seed;
    }
}
