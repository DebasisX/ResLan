#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <input.json> <output_base_name>\n", argv[0]);
        return 1;
    }

    const char *json_in = argv[1];
    const char *out_base = argv[2];

    char cmd[4096];
    int n = snprintf(cmd, sizeof(cmd),
                     "python3 resume.py %s %s.pdf",
                     json_in, out_base);
    if (n < 0 || n >= (int)sizeof(cmd)) {
        fprintf(stderr, "Error! \n");
        return 1;
    }

    int rc = system(cmd);
    if (rc == -1) {
        fprintf(stderr, "Failed! %s\n", strerror(errno));
        return 1;
    }
    return WEXITSTATUS(rc);
}
