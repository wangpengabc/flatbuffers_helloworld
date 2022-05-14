SRCS := \
monster_data.cc\
test.cc

# OJBS=$(SRCS:.cc=.o)
OBJS=$(patsubst %.cc,%.o,$(SRCS))

all: ${PROGS}

$(OBJS):%.o:%.cc
	g++ -o $@ -c $< -I/home/wangpeng/Downloads/flatbuffers/flatbuffers/include

test:$(OBJS)
	g++ -o $@ $^ -lstdc++


generate_bin_from_json:
	flatc --binary monster.fbs monsterdata.json

generate_hdr_from_fbs:
	flatc --cpp monster.fbs

generate_cpp_from_bin:
	python generate_cc_array.py 
