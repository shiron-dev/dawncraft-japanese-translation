import signal
import sys
import util
import dawncraft

def sig_handler(signum, frame):
    sys.exit(1)

def cleanup():
    print("Cleaning up...")
    # util.rm_tmp()
    
    # ls util.tmp_dir
    print(util.tmp_dir)
    


def main():
    signal.signal(signal.SIGTERM, sig_handler)
    try:
      print("DawnCraft Japanese Translator...")
      dawn_path = input("Enter the path to the DawnCraft folder: ")
      dawncraft.trans(dawn_path)

    finally:
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        cleanup()
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == "__main__":
    main()
