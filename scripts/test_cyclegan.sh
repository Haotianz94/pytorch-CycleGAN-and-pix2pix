set -ex
python3 test.py --dataroot ./datasets/maps --name maps_cyclegan --model cycle_gan --no_dropout --gpu_ids 0 --num_test 100000 
